import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:flutter/material.dart';

class AddMenu extends StatefulWidget {
  const AddMenu({super.key});

  @override
  State<AddMenu> createState() => _AddMenuState();
}

class _AddMenuState extends State<AddMenu> {
  TextEditingController name = TextEditingController();
  TextEditingController price = TextEditingController();

  addMenu() async {
    var url = 'http://172.30.1.35:3000/create/menu';
    var body = {
      "name": name.text.toString(),
      "price": price.text.toString(),
    };

    var data = await http.post(Uri.parse(url),
        body: json.encode(body),
        headers: {"Content-Type": "application/json"},
        encoding: Encoding.getByName("utf-8"));

    if (data.statusCode == 200) {
      Navigator.of(context).pop();
    } else {
      throw Exception('Failed to load data');
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        backgroundColor: Color.fromARGB(255, 255, 255, 255),
        appBar: AppBar(
          leading: IconButton(
            icon: Icon(Icons.arrow_back_ios),
            onPressed: () {
              Navigator.of(context).pop();
            },
          ),
          backgroundColor: Color(0xFF00704A),
          title: Text('Add menu'),
          actions: [
            Padding(
              padding: const EdgeInsets.all(8.0),
              child: ElevatedButton(
                  style: ElevatedButton.styleFrom(
                      primary: Color.fromARGB(255, 102, 52, 14)),
                  onPressed: () {
                    addMenu();
                  },
                  child: Text('Confirm')),
            )
          ],
        ),
        body: Container(
          child: Padding(
            padding: const EdgeInsets.all(20.0),
            child: Column(
              mainAxisAlignment: MainAxisAlignment.start,
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                const Text(
                  "Menu Name",
                  style: TextStyle(
                      color: Colors.black, fontWeight: FontWeight.bold),
                ),
                const SizedBox(
                  height: 5,
                ),
                TextField(
                  controller: name,
                  decoration: InputDecoration(
                      border: OutlineInputBorder(
                        borderRadius: BorderRadius.circular(10.0),
                      ),
                      filled: true,
                      focusColor: const Color(0xFF00704A),
                      hoverColor: const Color(0xFF00704A),
                      hintStyle: TextStyle(color: Colors.grey[800]),
                      hintText: "Menu name",
                      fillColor: Colors.white),
                ),
                SizedBox(
                  height: 20,
                ),
                const Text(
                  "Menu price",
                  style: TextStyle(
                      color: Colors.black, fontWeight: FontWeight.bold),
                ),
                const SizedBox(
                  height: 5,
                ),
                TextField(
                  controller: price,
                  decoration: InputDecoration(
                      border: OutlineInputBorder(
                        borderRadius: BorderRadius.circular(10.0),
                      ),
                      filled: true,
                      focusColor: const Color(0xFF00704A),
                      hoverColor: const Color(0xFF00704A),
                      hintStyle: TextStyle(color: Colors.grey[800]),
                      hintText: "Menu price",
                      fillColor: Colors.white),
                ),
              ],
            ),
          ),
        ));
  }
}
