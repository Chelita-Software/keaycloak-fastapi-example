"use client";
import { useAppDispatch, useAppSelector } from "@/lib/hooks";

import styles from "../styles/layout.module.css";

export default function HomePage() {
  const { data } = useAppSelector((state) => state.auth);

  return (
    <div className={styles.containerLogin}>
      <h1>Welcome to home {data.given_name}</h1>
      <h2>Your keycloak id: {data.sub}</h2>
      <p>
        You are succesfully logged in, navigate to your account in keycloak:
      </p>
      <a href="http://keycloak:8080/realms/fast-api/account" target="_blank">
        Click here
      </a>
      <p>
        Or <a href="http://fast-api:8001/auth/logout">logout</a>
      </p>
    </div>
  );
}
