https://github.com/user-attachments/assets/de25218c-6c42-4546-a673-4095cd63cda2


# AI-Based Tyre Pattern Detection and Automatic Sorting System

## Overview
This project implements an Industry 4.0 automated tyre sorting system using
Computer Vision and Embedded Systems.

A Convolutional Neural Network (CNN) is used to detect tyre tread patterns
in real-time using a camera. Based on the classification result, an Arduino
controls a conveyor system and servo motors to sort tyres automatically.

## Features
- Real-time tyre pattern classification using CNN
- Automatic conveyor control
- Servo-based sorting mechanism
- IR sensor detection for precise sorting
- Python-Arduino serial communication
- Industrial automation prototype

## Technologies Used
- Python
- TensorFlow / Keras
- OpenCV
- Arduino
- Computer Vision
- Embedded Systems

## System Architecture

Camera → CNN Model → Python Controller → Serial Communication → Arduino → Conveyor + Servo Sorting

## Classes Detected
- Straight Pattern Tyre
- Zigzag Pattern Tyre
- Empty Conveyor

## Hardware Components
- Arduino Uno
- USB Camera
- IR Sensors
- Servo Motors
- Relay Module
- Conveyor Belt Prototype

## How It Works

1. Camera captures tyre image.
2. CNN model classifies tyre pattern.
3. Python sends command to Arduino:
   - S → Straight Tyre
   - Z → Zigzag Tyre
   - E → Empty Conveyor
4. Arduino activates conveyor and sorting servo.
5. IR sensor triggers sorting mechanism.

## Installation

Install dependencies:
