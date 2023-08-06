package com.soap.ws;
import java.rmi.RemoteException;

import javax.xml.ws.Endpoint;

public class ServerBank_C {
	public static void main(String[] args) throws RemoteException {
		
		Endpoint.publish("http://192.168.1.8:1525/WS/Bank_C", new Bank_C());
		System.out.println("Servidor conectado...");
	}
}
	