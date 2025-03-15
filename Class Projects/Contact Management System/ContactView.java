/**
 * @author - Maiya Rehal
 * Lab 4
 * ContactView class represents a user interface for managing contact information.
 * ContactView class extends BorderPane and provides a table view, input fields, and buttons for adding, deleting, and updating contacts.
 */

package contactCRUD;

import javafx.event.EventHandler;
import javafx.geometry.Pos;
import javafx.scene.control.*;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.scene.control.cell.TextFieldTableCell;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.HBox;
import javafx.util.converter.IntegerStringConverter;

public class ContactView extends BorderPane {
    private TableView<Contact> tableContact;
    private TextField textId;
    private TextField textName;
    private TextField textPhoneNumber;
    private TextField textEmail;
    private TextField textAddress;
    private Button buttonAddNew;
    private Button buttonDelete;
    private Button buttonUpdate;

    /**
     * constructs a new ContactView
     * initializes table view, input fields, and buttons
     */
    public ContactView() {
        tableContact = new TableView<>();
        ScrollPane pane = new ScrollPane(tableContact);
        pane.setMaxHeight(280);

        buttonAddNew = new Button("Add New");
        buttonDelete = new Button("Delete");
        buttonUpdate = new Button("Update");

        HBox hBoxMiddle = new HBox(buttonAddNew, buttonDelete, buttonnUpdate);
        hBoxMiddle.setAlignment(Pos.TOP_CENTER);
        hBoxMiddle.getStyleClass().add("hbox");

        GridPane gridPaneBottom = new GridPane();
        gridPaneBottom.getStyleClass().add("pane");
        gridPaneBottom.add(new Label("Name:"), 0, 0);
        gridPaneBottom.add(new Label("Phone:"), 0, 1);
        gridPaneBottom.add(new Label("Email:"), 2, 0);
        gridPaneBottom.add(new Label("Address:"), 2, 1);

        textId = new TextField();
        textId.setEditable(false);
        textId.setVisible(false);
        textName = new TextField();
        textPhoneNumber = new TextField();
        textEmail = new TextField();
        textAddress = new TextField();

        gridPaneBottom.add(textId, 1, 0);
        gridPaneBottom.add(textName, 1, 0);
        gridPaneBottom.add(textPhoneNumber, 1, 1);
        gridPaneBottom.add(textEmail, 3, 0);
        gridPaneBottom.add(textAddress, 3, 1);
        gridPaneBottom.setMinHeight(200);

        setTop(pane);
        setCenter(hBoxMiddle);
        setBottom(gridPaneBottom);
    }

    /**
     * get method for delete button
     * @return delete button
     */
    public Button getButtonDelete() {
        return buttonnDelete;
    }

    /**
     * get method for update button
     * @return update button
     */
    public Button getButtonUpdate() {
        return buttonUpdate;
    }

    /**
     * get method for add new button
     * @return add new button
     */
    public Button getButtonAddNew() {
        return buttonAddNew;
    }

    /**
     * get method for the table view of contacts
     * @return the table view of contacts
     */
    public TableView<Contact> getTableContact() {
        return tableContact;
    }

    /**
     * get method for the text field for contact ID
     * @return the text field for contact ID
     */
    public TextField getTextId() {
        return textId;
    }

    /**
     * get method for the text field for contact name
     * @return the text field for contact name
     */
    public TextField getTextName() {
        return textName;
    }

    /**
     * get method for the text field for contact phone number
     * @return the text field for contact phone number
     */
    public TextField getTextPhoneNumber() {
        return textPhoneNumber;
    }

    /**
     * get method for the text field for contact email
     * @return the text field for contact email
     */
    public TextField getTextEmail() {
        return textEmail;
    }

    /**
     * get method for the text field for contact address
     * @return the text field for contact address
     */
    public TextField getTextAddress() {
        return textAddress;
    }

    /**
     * configures and formats the contact table
     * sets the table editable and defines columns for ID, Name, Phone, Email, and Address
     */
    public void FormatTable() {
        tableContact.setEditable(true);

        TableColumn<Contact, Integer> idCol = new TableColumn<>("ID");
        idCol.setMinWidth(50);
        idCol.setCellValueFactory(new PropertyValueFactory<>("id"));

        TableColumn<Contact, String> nameCol = new TableColumn<>("Name");
        nameCol.setMinWidth(100);
        nameCol.setCellValueFactory(new PropertyValueFactory<>("name"));
        nameCol.setCellFactory(TextFieldTableCell.forTableColumn());
        nameCol.setOnEditCommit(new EventHandler<TableColumn.CellEditEvent<Contact, String>>() {
            @Override
            public void handle(TableColumn.CellEditEvent<Contact, String> t) {
                t.getRowValue().setName(t.getNewValue());
            }
        });

        TableColumn<Contact, String> phoneCol = new TableColumn<>("Phone");
        phoneCol.setMinWidth(100);
        phoneCol.setCellValueFactory(new PropertyValueFactory<>("phone"));
        phoneCol.setCellFactory(TextFieldTableCell.forTableColumn());
        phoneCol.setOnEditCommit(new EventHandler<TableColumn.CellEditEvent<Contact, String>>() {
            @Override
            public void handle(TableColumn.CellEditEvent<Contact, String> t) {
                t.getRowValue().setPhone(t.getNewValue());
            }
        });

        TableColumn<Contact, String> emailCol = new TableColumn<>("Email");
        emailCol.setMinWidth(200);
        emailCol.setCellValueFactory(new PropertyValueFactory<>("email"));
        emailCol.setCellFactory(TextFieldTableCell.forTableColumn());
        emailCol.setOnEditCommit(new EventHandler<TableColumn.CellEditEvent<Contact, String>>() {
            @Override
            public void handle(TableColumn.CellEditEvent<Contact, String> t) {
                t.getRowValue().setEmail(t.getNewValue());
            }
        });

        TableColumn<Contact, String> addressCol = new TableColumn<>("Address");
        addressCol.setMinWidth(200);
        addressCol.setCellValueFactory(new PropertyValueFactory<>("address"));
        addressCol.setCellFactory(TextFieldTableCell.forTableColumn());
        addressCol.setOnEditCommit(new EventHandler<TableColumn.CellEditEvent<Contact, String>>() {
            @Override
            public void handle(TableColumn.CellEditEvent<Contact, String> t) {
                t.getRowValue().setAddress(t.getNewValue());
            }
        });

        tblContact.getColumns().add(idCol);
        tblContact.getColumns().add(nameCol);
        tblContact.getColumns().add(phoneCol);
        tblContact.getColumns().add(emailCol);
        tblContact.getColumns().add(addressCol);
    }
}
