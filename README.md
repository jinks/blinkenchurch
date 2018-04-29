# Python Script for controlling VBS lighting modules from a Raspberry Pi

## Written By Les Holdeman 02/2018

Python documentation:

* smbus - https://pypi.python.org/pypi/smbus2/0.2.0
* socket - https://docs.python.org/2/library/socket.html
* time - https://docs.python.org/2/library/time.html

Other sources:
* http://www.steves-internet-guide.com/into-mqtt-python-client/
* paho.mqtt.client - https://www.eclipse.org/paho/

## Commands for various colors of each LED

* LED 1

  | colour     | regA | codeA | regB | codeB |
  | ---        | ---  | ---   | ---  | ---   |
  | red        | 0x14 | 0x01  |      |       |
  | green      | 0x14 | 0x02  |      |       |
  | yellow     | 0x14 | 0x03  |      |       |
  | blue       | 0x14 | 0x04  |      |       |
  | purple     | 0x14 | 0x05  |      |       |
  | light Blue | 0x14 | 0x06  |      |       |
  | white      | 0x14 | 0x07  |      |       |

* LED 2

  | colour     | regA | codeA | regB | codeB |
  | ---        | ---  | ---   | ---  | ---   |
  | red        | 0x14 | 0x08  |      |       |
  | green      | 0x14 | 0x10  |      |       |
  | yellow     | 0x14 | 0x18  |      |       |
  | blue       | 0x14 | 0x20  |      |       |
  | purple     | 0x14 | 0x28  |      |       |
  | light Blue | 0x14 | 0x30  |      |       |
  | white      | 0x14 | 0x38  |      |       |

* LED 3

  | colour     | regA | codeA | regB | codeB |
  | ---        | ---  | ---   | ---  | ---   |
  | red        | 0x14 | 0x40  |      |       |
  | green      | 0x14 | 0x80  |      |       |
  | yellow     | 0x14 | 0xC0  |      |       |
  | blue       |      |       | 0x15 | 0x01  |
  | purple     | 0x14 | 0x40  | 0x15 | 0x01  |
  | light Blue | 0x14 | 0x80  | 0x15 | 0x01  |
  | white      | 0x14 | 0xC0  | 0x15 | 0x01  |

* LED 4

  | colour     | regA | codeA | regB | codeB |
  | ---        | ---  | ---   | ---  | ---   |
  | red        |      |       | 0x15 | 0x02  |
  | green      |      |       | 0x15 | 0x04  |
  | yellow     |      |       | 0x15 | 0x06  |
  | blue       |      |       | 0x15 | 0x08  |
  | purple     |      |       | 0x15 | 0x0A  |
  | light Blue |      |       | 0x15 | 0x0C  |
  | white      |      |       | 0x15 | 0x0E  |

* LED 5

  | colour     | regA | codeA | regB | codeB |
  | ---        | ---  | ---   | ---  | ---   |
  | red        |      |       | 0x15 | 0x10  |
  | green      |      |       | 0x15 | 0x20  |
  | yellow     |      |       | 0x15 | 0x30  |
  | blue       |      |       | 0x15 | 0x40  |
  | purple     |      |       | 0x15 | 0x50  |
  | light Blue |      |       | 0x15 | 0x60  |
  | white      |      |       | 0x15 | 0x70  |

* Standby

  | colour     | regA | codeA | regB | codeB |
  | ---        | ---  | ---   | ---  | ---   |
  | cycle      |      |       | 0x15 | 0x80  |
