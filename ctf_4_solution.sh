#!/bin/bash

# Define the IP address and port
IP_ADDRESS="LAPTOP-IPLBIJ78"
PORT=23456

# Run the Python program in a loop to create 100 connections
for ((i=1; i<=100; i++))
do
    python connect.py $IP_ADDRESS $PORT &
done

# Wait for all processes to finish
wait
echo "All connections established"
