package com.soap.ws;

public class Usuario {

	private String nombre;
	private String n_cuenta;	   
	private float saldo = 0;

	public String getNombre() {
		return nombre;
	}
	public void setNombre(String nombre) {
		this.nombre = nombre;
	}
	public String getN_cuenta() {
		return n_cuenta;
	}
	public void setN_cuenta(String n_cuenta) {
		this.n_cuenta = n_cuenta;
	}		
	public float getSaldo() {
		return saldo;
	}
	public void setSaldo(float saldo) {
		this.saldo = saldo;
	}

}