"use client";
import styles from "../styles/layout.module.css";

export default function HomePage() {
  return (
    <div className={styles.containerLogin}>
      <h1>Welcome to home</h1>
      <p>You are succesfully logged in, navigate to your account in keycloak:</p>
      <a href="http://keycloak:8080/realms/fast-api/account" target="_blank">Click here</a>
    </div>
  );
}

