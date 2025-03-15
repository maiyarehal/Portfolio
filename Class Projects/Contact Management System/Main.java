package Contact_Managament_System;

import javafx.application.Application;
import javafx.collections.*;
import javafx.scene.Scene;
import javafx.stage.Stage;

public class MainApp extends Application {
    private ContactView contactView;
    private ObservableList<Contact> contactList;
    private ContactDAO contactDAO;

    @Override
    public void start(Stage primaryStage) {
        contactView = new ContactView();
        contactDAO = new ContactDAO();
        contactList = FXCollections.observableArrayList(contactDAO.findAll());
        contactView.getTblContact().setItems(contactList);
        contactView.FormatTable();

        contactView.getButtonAddNew().setOnAction(e -> addNewContact());
        contactView.getButtonDelete().setOnAction(e -> deleteContact());
        contactView.getButtonUpdate().setOnAction(e -> updateContact());

        Scene scene = new Scene(contactView, 600, 400);
        primaryStage.setTitle("Contact Management");
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    private void addNewContact() {
        Contact c = new Contact();
        c.setName(contactView.getTextName().getText());
        c.setPhone(contactView.getTextPhoneNumber().getText());
        c.setEmail(contactView.getTextEmail().getText());
        c.setAddress(contactView.getTextAddress().getText());
        if (contactDAO.create(c)) {
            contactList.add(c);
            clearInputFields();
        }
    }

    private void updateContact() {
        Contact selected = contactView.getTableContact().getSelectionModel().getSelectedItem();
        if (selected != null) {
            selected.setName(contactView.getTextName().getText());
            selected.setPhone(contactView.getTextPhoneNumber().getText());
            selected.setEmail(contactView.getTextEmail().getText());
            selected.setAddress(contactView.getTextAddress().getText());
            if (contactDAO.update(selected)) {a
                contactList.set(contactList.indexOf(selected), selected);
                clearInputFields();
            }
        }
    }

    private void deleteContact() {
        Contact selected = contactView.getTableContact().getSelectionModel().getSelectedItem();
        if (selected != null) {
            if (contactDAO.delete(selected)) {
                contactList.remove(selected);
                clearInputFields();
            }
        }
    }

    private void clearInputFields() {
        contactView.getTextName().clear();
        contactView.getTextPhoneNumber().clear();
        contactView.getTextEmail().clear();
        contactView.getTextAddress().clear();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
