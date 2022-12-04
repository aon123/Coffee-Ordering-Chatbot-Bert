import 'package:coffee_app/pages/Order.dart';
import 'package:coffee_app/pages/admin.dart';
import 'package:flutter/material.dart';

import 'package:bottom_navy_bar/bottom_navy_bar.dart';

class Home extends StatefulWidget {
  const Home({super.key});

  @override
  State<Home> createState() => _HomeState();
}

class _HomeState extends State<Home> {
  int _currentIndex = 0;

  Widget? currentPage;

  @override
  void initState() {
    // TODO: implement initState
    super.initState();
    currentPage = AdminPage();
  }

  void SelectPage(index) {
    if (index == 0) {
      setState(() {
        _currentIndex = index;
        currentPage = AdminPage();
      });
    } else if (index == 1) {
      setState(() {
        _currentIndex = index;
        currentPage = OrderPage();
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      bottomNavigationBar: BottomNavyBar(
        selectedIndex: _currentIndex,
        showElevation: true,
        itemCornerRadius: 14,
        curve: Curves.easeInSine,
        onItemSelected: (index) => SelectPage(index),
        items: <BottomNavyBarItem>[
          BottomNavyBarItem(
            icon: Icon(Icons.person),
            title: Text('Admin'),
            activeColor: Color(0xFF00704A),
            textAlign: TextAlign.center,
          ),
          BottomNavyBarItem(
            icon: Icon(Icons.apps),
            title: Text('Orders'),
            activeColor: Color(0xFF00704A),
            textAlign: TextAlign.center,
          ),
        ],
      ),
      body: currentPage,
    );
  }
}
