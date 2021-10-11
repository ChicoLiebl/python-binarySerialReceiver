# Serial Receiver

Simple module for receiving binary data from a serial port in an asynchronous form

## Description

This modules lets you specify the format of the binary data and the header to be received from a serial port. The module creates a dedicated thread to read de serial port and feed the numpy arrays passed as buffers in a circular forma, always keeping the same length.

## Example

In the example folder there is a script that creates a virtual serial port (works only on linux) allowing you to run test-receiver.py which will print the received data buffer.