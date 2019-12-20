//This interface will give us the flexibility to plug in other types of switches,
// say a remote control switch later on, if required.
interface Switch{
	public boolean isOn();
	public void press();
}

// any switchable device can implement this interface and get the functionality
interface Switchable{
	public void turnOn();
	public void turnOff();
}

//high level class 
class EletricSwitch implements Switch{
	private Switchable device;
	private boolean on;
	
	public EletricSwitch(Switchable device){
		this.device = device;
		this.on = false;
	}
	
	public boolean isOn(){
		return this.on;
	}
	
	public void press(){
		boolean checkOn = isOn();
		if(checkOn){
			device.turnOff();
			this.on = false;
		}
		else{
			device.turnOn();
			this.on = true;
		}
	}
}

//low level class
class ligntBulb implements Switchable{
	public void turnOn(){
		System.out.println("LightBulb is turned on.");
	}
	
	public void turnOff(){
		System.out.println("LightBulb is turned off.");
	}
}

//low level class
class Fan implements Switchable{
	public void turnOn(){
		System.out.println("Fan is turned on.");
	}
	
	public void turnOff(){
		System.out.println("Fan is turned off.");
	}
}



