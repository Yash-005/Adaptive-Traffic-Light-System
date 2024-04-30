# Adaptive Traffic Light System

The Adaptive Traffic Light System is a project designed to optimize traffic flow at intersections by dynamically adjusting traffic signal timings based on real-time traffic conditions. This system utilizes computer vision techniques for vehicle detection and tracking to gather data on traffic volume and flow.

## Overview

The project consists of three main components:

1. **Stream Module**: Responsible for capturing video feeds from traffic cameras placed at different lanes of the intersection.
2. **Counter Module**: Implements object detection and vehicle counting algorithms to analyze the traffic data obtained from the stream module.
3. **Main Module**: Integrates the functionalities of the stream and counter modules to control the traffic lights based on the vehicle counts from each lane.

## Getting Started

### Prerequisites

- Python 3.x
- OpenCV (cv2)
- NumPy

### Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/Yash-005/adaptive-traffic-light-system.git
    ```

2. install the required libraries and Yolo V3 weights
    ```

### Usage

1. Place video files capturing traffic from each lane in the `stream` directory.
2. Adjust the configuration files (`modelConfiguration` and `modelWeights`) in the `counter.py` script to point to the YOLOv3 model files.
3. Run the `main.py` script to start the adaptive traffic light system:

    ```bash
    python main.py
    ```

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push your changes to your forked repository (`git push origin feature/your-feature-name`).
5. Create a new pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This project was inspired by the need to improve traffic management at busy intersections.
---

Feel free to customize this README file according to your project's specific details and requirements.
