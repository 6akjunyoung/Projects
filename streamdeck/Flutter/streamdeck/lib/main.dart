import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Responsive Button and Slider Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: ButtonSliderPage(),
    );
  }
}

class ButtonSliderPage extends StatefulWidget {
  @override
  _ButtonSliderPageState createState() => _ButtonSliderPageState();
}

class _ButtonSliderPageState extends State<ButtonSliderPage> {
  List<int> buttonValues = List<int>.filled(8, 0);
  double sliderValue = 1.0;

  // 버튼 숫자 증가
  void incrementButtonValue(int index) {
    setState(() {
      buttonValues[index] += sliderValue.toInt();
    });
  }

  // 버튼 숫자 감소
  void decrementButtonValue(int index) {
    setState(() {
      buttonValues[index] -= sliderValue.toInt();
    });
  }

  // 슬라이더 값 업데이트
  void updateSlider(double newValue) {
    setState(() {
      sliderValue = newValue;
    });
  }

  // 버튼 빌드 함수
  Widget buildButton(int index) {
    return Column(
      mainAxisAlignment: MainAxisAlignment.center,
      children: [
        Text(
          'Button ${index + 1}',
          style: TextStyle(fontSize: 18),
        ),
        Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            IconButton(
              icon: Icon(Icons.remove),
              onPressed: () => decrementButtonValue(index),
            ),
            Text(
              '${buttonValues[index]}',
              style: TextStyle(fontSize: 24),
            ),
            IconButton(
              icon: Icon(Icons.add),
              onPressed: () => incrementButtonValue(index),
            ),
          ],
        ),
      ],
    );
  }

  @override
  Widget build(BuildContext context) {
    // 화면 크기를 가져와서 가로/세로 비율을 계산
    var size = MediaQuery.of(context).size;
    var aspectRatio = size.width / size.height;

    // 가로/세로 비율에 따라 버튼이 배치될 열 수 결정
    int crossAxisCount = aspectRatio > 1.0 ? 4 : 2;

    return Scaffold(
      appBar: AppBar(
        title: Text('Responsive Button and Slider Demo'),
      ),
      body: ListView(
        children: [
          // 8개의 버튼을 그리드 형태로 배치
          GridView.builder(
            shrinkWrap: true, // 그리드 뷰가 다른 스크롤 뷰 안에 있을 때 크기를 맞춤
            physics: NeverScrollableScrollPhysics(), // 그리드 뷰 자체의 스크롤 비활성화
            gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
              crossAxisCount: crossAxisCount, // 가로/세로 비율에 따라 열 수 결정
              childAspectRatio: 2, // 버튼 비율 (조정 가능)
            ),
            itemCount: 8,
            itemBuilder: (context, index) {
              return Padding(
                padding: const EdgeInsets.all(8.0),
                child: Card(
                  elevation: 4,
                  child: buildButton(index),
                ),
              );
            },
          ),
          // 슬라이더
          Padding(
            padding: const EdgeInsets.symmetric(horizontal: 20.0, vertical: 20.0),
            child: Column(
              children: [
                Text(
                  'Slider Value: ${sliderValue.toInt()}',
                  style: TextStyle(fontSize: 18),
                ),
                Slider(
                  value: sliderValue,
                  min: 1,
                  max: 10,
                  divisions: 9,
                  label: sliderValue.toInt().toString(),
                  onChanged: updateSlider,
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
