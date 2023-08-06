package com.soap.ws;

import java.rmi.RemoteException;

import javax.jws.WebMethod;
import javax.jws.WebService;

@WebService
public interface RemoteInterface {
	@WebMethod
	public void crearCuenta(String nombre) throws RemoteException;
	
    public String generarCodigo() throws RemoteException;
	
    public void listaUsuarios() throws RemoteException;
	
    public void deposito(String nCuenta, float x) throws RemoteException;
	
	public void retiro(String nCuenta, float x) throws RemoteException;
	
	public void transferencia(String nCuentaX, float x, String nCuentaY) throws RemoteException;
	
    public String detalle(String nCuenta) throws RemoteException;

}