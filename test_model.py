import numpy as np
import re
import torch
import torch.nn as nn
from sklearn.preprocessing import LabelEncoder
from transformers import AutoModel, BertTokenizerFast# Load the BERT tokenizer
tokenizer = BertTokenizerFast.from_pretrained('bert-base-uncased')# Import BERT-base pretrained model
bert = AutoModel.from_pretrained('bert-base-uncased')

le = LabelEncoder()
device = torch.device('cpu')


class BERT_Arch(nn.Module):
    
    def __init__(self, bert):
        super(BERT_Arch, self).__init__()
        self.bert=bert
        self.dropout = nn.Dropout(0.5)
        self.relu = nn.ReLU()
        self.fc1 = nn.Linear(768,512)
        self.fc2 = nn.Linear(512, 256)
        self.fc3 = nn.Linear(256, 4)
        self.softmax = nn.LogSoftmax(dim=1)
        
    def forward(self, sent_id, mask):
        cls_hs = self.bert(sent_id, attention_mask=mask)[0][:,0]
        
        x = self.fc1(cls_hs)
        x = self.relu(x)
        x = self.dropout(x)
        
        x = self.fc2(x)
        x = self.relu(x)
        x = self.dropout(x)
        
        x = self.fc3(x)
        
        x = self.softmax(x)
        
        return x



labels = {0: 'order', 1: 'size',  2: 'greeting', 3: 'thank'}

def get_prediction(str):
    str = re.sub(r'[^a-zA-Z]+', '', str)
    test_text = [str]
    model.eval()
    
    tokens_test_data = tokenizer(
        test_text,
        max_length = 8,
        padding = True,
        truncation=True,
        return_token_type_ids = False
    )
    
    test_seq = torch.tensor(tokens_test_data['input_ids'])
    test_mask = torch.tensor(tokens_test_data['attention_mask'])

    preds = None 
    with torch.no_grad():
        preds = model(test_seq.to(device), test_mask.to(device))
    
    preds = preds.detach().cpu().numpy()
    preds = np.argmax(preds, axis = 1)
    return preds[0]


PATH='/Users/aon97/programming/chatbot/model/chatbotmodel.pth'
model = BERT_Arch(bert)
model.load_state_dict(torch.load(PATH))
model = model.to(device)



    

    