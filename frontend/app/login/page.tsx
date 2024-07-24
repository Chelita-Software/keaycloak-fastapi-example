"use client";
import { useRouter } from "next/navigation";

import styles from "../styles/layout.module.css";

export default function IndexPage() {
  const router = useRouter();
  const login = () => {
    router.push("http://fast-api:8001/auth/login");
  }

  return (
    <div className={styles.containerLogin}>
      <h1>Welcome to the Keycloak integration example</h1>
      <h2>Click to Login</h2>
      <button onClick={login}>Login</button>
    </div>
  );
}

