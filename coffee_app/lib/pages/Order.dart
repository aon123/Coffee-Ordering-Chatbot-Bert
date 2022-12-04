import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

class OrderPage extends StatefulWidget {
  const OrderPage({super.key});

  @override
  State<OrderPage> createState() => _OrderPageState();
}

class _OrderPageState extends State<OrderPage> {
  List? data;

  getOrder() async {
    final response = await http.get(Uri.parse('http://172.30.1.35:3000/order'));
    if (response.statusCode == 200) {
      setState(() {
        data = json.decode(response.body);
      });
    } else {
      throw Exception('Failed to load data');
    }
  }

  ready(id) async {
    var url = 'http://172.30.1.35:3000/ready';
    var body = {
      "_id": id,
    };

    var data = await http.post(Uri.parse(url),
        body: json.encode(body),
        headers: {"Content-Type": "application/json"},
        encoding: Encoding.getByName("utf-8"));

    if (data.statusCode == 200) {
      getOrder();
    } else {
      throw Exception('Failed to load data');
    }
  }

  @override
  void initState() {
    // TODO: implement initState
    super.initState();
    getOrder();
  }

  @override
  Widget build(BuildContext context) {
    if (data != null) {
      return Scaffold(
          backgroundColor: Color.fromARGB(255, 255, 255, 255),
          appBar: AppBar(
            backgroundColor: Color(0xFF00704A),
            title: Text('Orders'),
          ),
          body: Container(
              child: ListView.builder(
            itemCount: data!.length,
            itemBuilder: ((context, index) {
              if (data![index]['status'] != 'Ready') {
                return Padding(
                  padding: const EdgeInsets.all(10.0),
                  child: Container(
                    width: MediaQuery.of(context).size.width,
                    height: MediaQuery.of(context).size.height * 0.23,
                    decoration: BoxDecoration(
                        color: Color.fromARGB(255, 255, 255, 255),
                        boxShadow: [
                          BoxShadow(
                            color: Colors.grey.withOpacity(0.5),
                            spreadRadius: 2,
                            blurRadius: 3,
                            offset: Offset(0, 3), // changes position of shadow
                          ),
                        ],
                        borderRadius: BorderRadius.circular(10.0)),
                    child: Padding(
                      padding: const EdgeInsets.all(20.0),
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.center,
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: [
                          Row(
                            mainAxisAlignment: MainAxisAlignment.spaceBetween,
                            children: [
                              Text(
                                'Date',
                                style: TextStyle(fontWeight: FontWeight.w600),
                              ),
                              Text(
                                data![index]['date'],
                                style: TextStyle(fontWeight: FontWeight.w600),
                              )
                            ],
                          ),
                          SizedBox(
                            height: 10,
                          ),
                          Row(
                            mainAxisAlignment: MainAxisAlignment.spaceBetween,
                            children: [
                              Text(
                                'Customer id',
                                style: TextStyle(fontWeight: FontWeight.w600),
                              ),
                              Text(
                                data![index]['_id'],
                                style: TextStyle(fontWeight: FontWeight.w600),
                              )
                            ],
                          ),
                          SizedBox(
                            height: 10,
                          ),
                          Row(
                            mainAxisAlignment: MainAxisAlignment.spaceBetween,
                            children: [
                              Text(
                                'Order Name',
                                style: TextStyle(fontWeight: FontWeight.w600),
                              ),
                              Text(
                                data![index]['name'],
                                style: TextStyle(fontWeight: FontWeight.w600),
                              )
                            ],
                          ),
                          SizedBox(
                            height: 10,
                          ),
                          Row(
                            mainAxisAlignment: MainAxisAlignment.spaceBetween,
                            children: [
                              Text(
                                'Order size',
                                style: TextStyle(fontWeight: FontWeight.w600),
                              ),
                              Text(
                                data![index]['size'],
                                style: TextStyle(fontWeight: FontWeight.w600),
                              )
                            ],
                          ),
                          SizedBox(
                            height: 10,
                          ),
                          Row(
                            mainAxisAlignment: MainAxisAlignment.spaceBetween,
                            children: [
                              Text(
                                'Status',
                                style: TextStyle(fontWeight: FontWeight.w600),
                              ),
                              ElevatedButton(
                                  style: ElevatedButton.styleFrom(
                                      primary:
                                          Color.fromARGB(255, 102, 52, 14)),
                                  onPressed: () {
                                    ready(data![index]['_id']);
                                  },
                                  child: const Text(
                                    'Ready',
                                    style:
                                        TextStyle(fontWeight: FontWeight.w600),
                                  ))
                            ],
                          ),
                        ],
                      ),
                    ),
                  ),
                );
              } else {
                // ignore: prefer_const_constructors
                return SizedBox(
                  width: 0,
                  height: 0,
                );
              }
            }),
          )));
    } else {
      return Scaffold(
        backgroundColor: Color.fromARGB(255, 255, 255, 255),
        appBar: AppBar(
          backgroundColor: Color(0xFF00704A),
          title: Text('Order'),
        ),
        body: Center(
            child: Text(
          'No orders!',
          style: TextStyle(
              color: Colors.grey[400],
              fontSize: 18,
              fontWeight: FontWeight.bold),
        )),
      );
    }
  }
}
