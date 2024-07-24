"use client";
import { useEffect } from "react";
import { useRouter } from "next/navigation";

import { useAppSelector } from "@/lib/hooks";

import styles from "../styles/layout.module.css";

export default function IndexPage() {
  const router = useRouter();
  const { isAuthenticated } = useAppSelector((state) => state.auth);

  useEffect(() => {
    if (isAuthenticated) {
      router.push("/home");
    }
  }, [isAuthenticated]);

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

