/**
 * @author - Maiya Rehal
 * Lab 4
 * Contact class represents a contact with an ID, Name, Phone Number, Email, and Address.
 * Uses JavaFX properties to allow for easy binding in JavaFX applications.
 */

package contactCRUD;

import javafx.beans.property.*;

public class Contact {
    private IntegerProperty id;
    private StringProperty name;
    private StringProperty phone;
    private StringProperty email;
    private StringProperty address;

    /**
     * default constructor for creating an empty Contact
     */
    public Contact() {}

    /**
     * constructs a Contact with specified ID, Name, Phone Number, Email, and Address
     * @param id - contact ID
     * @param name - contact name
     * @param phone - contact phone number
     * @param email - contact email address
     * @param address - contact address
     */
    public Contact(int id, String name, String phone, String email, String address) {
        this.id = new SimpleIntegerProperty(id);
        this.name = new SimpleStringProperty(name);
        this.phone = new SimpleStringProperty(phone);
        this.email = new SimpleStringProperty(email);
        this.address = new SimpleStringProperty(address);
    }

    /**
     * get method for contact ID
     * @return contact ID
     */
    public int getId() { 
    	return id.get(); 
    	}
    
    /**
     * get method for contact name
     * @return contact name
     */
    public String getName() { 
    	return name.get(); 
    	}
    
    /**
     * get method for contact phone number
     * @return contact phone number
     */
    public String getPhone() { 
    	return phone.get(); 
    	}
    
    /**
     * get method for contact email address
     * @return contact email address
     */
    public String getEmail() { 
    	return email.get(); 
    	}
    
    /**
     * get method for contact address
     * @return contact address
     */
    public String getAddress() { 
    	return address.get(); 
    	}

    /**
     * set method for contact ID
     * @param id - new contact ID
     */
    public void setId(int id) { 
    	this.id.set(id); 
    	}
    
    /**
     * set method for contact name
     * @param name - new contact name
     */
    public void setName(String name) { 
    	this.name.set(name); 
    	}
    
    /**
     * set method for contact phone number
     * @param phone - new contact phone number
     */
    public void setPhone(String phone) { 
    	this.phone.set(phone); 
    	}
    
    /**
     * set method for contact email address
     * @param email - new contact email address
     */
    public void setEmail(String email) { 
    	this.email.set(email); 
    	}
    
    /**
     * set method for contact address
     * @param address - new contact address
     */
    public void setAddress(String address) { 
    	this.address.set(address); 
    	}

    /**
     * returns a string representation of the Contact
     * @return string representation of Contact
     */
    @Override
    public String toString() {
        return "Contact [id=" + id.get() + ", name=" + name.get() + ", phone=" + phone.get() + ", email=" + email.get() + ", address=" + address.get() + "]";
    }
}
