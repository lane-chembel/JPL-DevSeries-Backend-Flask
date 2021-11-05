
<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



# Backend Flask Server

This is a simple `hello world` type OOP Flask application that can be used as a template for multiple uses.

Two endpoints with calls to a separate class returning JSON data to client.

Features:
* Docker enabled
* Flask v2.0.2
* Simple OOP
* 2 defined endpoints


### Building and Running with Docker
Note: This is not necessary if you are not using Docker.

* Build the docker container:
  ```
  docker build -t be:dev .
  ```

* Run the app through the container:
  ```
  docker run -it --rm -v $(PWD):/app -p 5001:5000 -e CHOKIDAR_USEPOLLING=true --name be --rm be:dev
  ```

### Non Dockerized Version

* Pre-requisite: 
  * Python 3
  * Pip 3

* Run in [virtual env](https://docs.python-guide.org/dev/virtualenvs/)

* Build the server
  ```
  pip3 install -r requirements.txt
  ```
* Run the server
  ```
  python3 app.py
  ```
### Test server response

* cURL ([Windows](https://stackoverflow.com/questions/9507353/how-do-i-install-and-use-curl-on-windows))
  ```
  curl http://localhost:5001/getSomeData
  curl http://localhost:5001/getSomeDataFromFile
  ```

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/issues/spaceshiptrip/DevSeries-Backend-Flask?style=for-the-badge
[contributors-url]: https://github.com/spaceshiptrip/TechInterview-Backend/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/spaceshiptrip/DevSeries-Backend-Flask?style=for-the-badge
[forks-url]: https://github.com/spaceshiptrip/TechInterview-Backend/network/members
[issues-shield]: https://img.shields.io/github/issues/spaceshiptrip/DevSeries-Backend-Flask?style=for-the-badge
[issues-url]: https://github.com/spaceshiptrip/TechInterview-Backend/issues
[license-shield]: https://img.shields.io/github/license/spaceshiptrip/DevSeries-Backend-Flask?style=for-the-badge
[license-url]: https://github.com/spaceshiptrip/DevSeries-Backend-Flask/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/jaytorres-robotics/
[product-screenshot]: images/screenshot.png
