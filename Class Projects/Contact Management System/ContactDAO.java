/**
 * @author - Maiya Rehal
 * Lab 4
 * ContactDAO class provides CRUD (create, read, update, and delete) operations for Contact objects using a database.
 */

package contactCRUD;

import java.sql.*;
import java.util.*;

public class ContactDAO {
    
	/**
	 * retrieves all contacts from database
	 * @return a list of all contacts
	 * @return null if error occurs
	 */
	public List<Contact> findAll() {
        try {
            List<Contact> listContacts = new ArrayList<>();
            PreparedStatement ps = DbConnection.getConnection().prepareStatement("SELECT * FROM Contact");
            ResultSet rs = ps.executeQuery();
            while (rs.next()) {
                int id = rs.getInt("id");
                String name = rs.getString("name");
                String phone = rs.getString("phone");
                String email = rs.getString("email");
                String address = rs.getString("address");
                Contact c = new Contact(id, name, phone, email, address);
                listContacts.add(c);
            }
            return listContacts;
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }

	/**
	 * retrieves a contact by its ID from database
	 * @param id - ID of contact to retrieve
	 * @return contact with specified ID
	 * @return null if contact not found or an error occurs
	 */
    public Contact find(int id) {
        try {
            Contact c = null;
            PreparedStatement ps = DbConnection.getConnection().prepareStatement("SELECT * FROM Contact WHERE id=?");
            ps.setInt(1, id);
            ResultSet rs = ps.executeQuery();
            if (rs.next()) {
                String name = rs.getString("name");
                String phone = rs.getString("phone");
                String email = rs.getString("email");
                String address = rs.getString("address");
                c = new Contact(id, name, phone, email, address);
            }
            return c;
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }

    /**
     * creates a new contact in database
     * @param c - contact to create
     * @return true if contact was added successfully
     * @return false if contact was added unsuccessfully
     */
    public boolean create(Contact c) {
        try {
            PreparedStatement ps = DbConnection.getConnection().prepareStatement(
                    "INSERT INTO Contact(name, phone, email, address) VALUES (?, ?, ?, ?)");
            ps.setString(1, c.getName());
            ps.setString(2, c.getPhone());
            ps.setString(3, c.getEmail());
            ps.setString(4, c.getAddress());
            return ps.executeUpdate() > 0;
        } catch (Exception e) {
            e.printStackTrace();
            return false;
        }
    }

    /**
     * updates existing contact information in database
     * @param c - contact to update
     * @return true if contact was updated successfully
     * @return false if contact was updated unsuccessfully
     */
    public boolean update(Contact c) {
        try {
            PreparedStatement ps = DbConnection.getConnection().prepareStatement(
                    "UPDATE Contact SET name=?, phone=?, email=?, address=? WHERE id=?");
            ps.setString(1, c.getName());
            ps.setString(2, c.getPhone());
            ps.setString(3, c.getEmail());
            ps.setString(4, c.getAddress());
            ps.setInt(5, c.getId());
            return ps.executeUpdate() > 0;
        } catch (Exception e) {
            e.printStackTrace();
            return false;
        }
    }

    /**
     * deletes contact from database
     * @param c - contact to delete
     * @return true is contact deleted successfully
     * @return false is contact deleted unsuccessfully
     */
    public boolean delete(Contact c) {
        try {
            PreparedStatement ps = DbConnection.getConnection().prepareStatement("DELETE FROM Contact WHERE id=?");
            ps.setInt(1, c.getId());
            return ps.executeUpdate() > 0;
        } catch (Exception e) {
            e.printStackTrace();
            return false;
        }
    }
}
