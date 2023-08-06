package com.soap.ws;
import java.rmi.RemoteException;
import javax.xml.ws.Endpoint;

public class ServerBank_A {
	public static void main(String[] args) throws  RemoteException {
		
		Endpoint.publish("http://192.168.1.4:1515/WS/Bank_A", new Bank_A());
		System.out.println("Servidor conectado...");
	}
}
	