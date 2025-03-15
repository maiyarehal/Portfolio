/**
 * @author - Maiya Rehal
 * Lab 4
 * DbConnection class provides methods to verify the database driver class
 * and establish a connection to the database.
 */

package contactCRUD;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class DbConnection {
	
	/**
	 * verify that the MySQL JDBC driver is loaded
	 * @return true if driver is loaded successfully
	 * @return false if driver is loaded unsuccessfully
	 */
    public static boolean VerifyDBClassLoaded() {
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            return true;
        } catch (ClassNotFoundException e) {
            return false;
        }
    }
    
    /**
     * establishes a connection to the MySQL database using specified URL, username, and password
     * @return Connection object if connection is successful
     * @return null if connection is unsuccessful 
     */
    public static Connection getConnection() {
        try {
            Connection conn = DriverManager.getConnection("jdbc:mysql://Documents/CSC251", "Maiya", "Rehal");
            return conn;
        } catch (SQLException e) {
            e.printStackTrace();
            return null;
        }
    }
}
