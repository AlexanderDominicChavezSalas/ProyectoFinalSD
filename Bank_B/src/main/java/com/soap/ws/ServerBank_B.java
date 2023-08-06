package com.soap.ws;
import java.rmi.RemoteException;

import javax.xml.ws.Endpoint;

public class ServerBank_B {
	public static void main(String[] args) throws RemoteException {
		
		Endpoint.publish("http://192.168.1.7:1520/WS/Bank_B", new Bank_B());
		System.out.println("Servidor conectado...");
	}
}
	