package com.soap.ws;
import java.util.ArrayList;
import java.util.List;

public class LockManager {
	private static LockManager single_instance = null;
	private static List<Usuario> accountLocks = new ArrayList<Usuario>();

	public static LockManager getInstance() {
		if (single_instance == null)
			single_instance = new LockManager();

		return single_instance;
	}

	private LockManager() {
		accountLocks.clear();
	}

	public boolean isLocked(Usuario account) {

		return accountLocks.contains(account);
	}
	
	public boolean isLocked() {

		return !accountLocks.isEmpty();
	}

	public void lock(Usuario account) {
		accountLocks.add(account);
	}

	public void unLock(Usuario account) {
		accountLocks.remove(account);
	}

	public void unLockAll() {
		accountLocks.clear();
	}
}
