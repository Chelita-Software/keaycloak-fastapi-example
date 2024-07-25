import type { ReactNode } from "react";
import { StoreProvider } from "./StoreProvider";
import AuthorizationContext from "./auth";
import Image from "next/image";

import "./styles/globals.css";
import styles from "./styles/layout.module.css";

interface Props {
  readonly children: ReactNode;
}

export default function RootLayout({ children }: Props) {
  return (
    <StoreProvider>
      <html lang="en">
        <body>
          <AuthorizationContext>
            <main className={styles.main}>
              <Image
                src="/chelita-logo.png"
                alt="logo"
                width="600"
                height="250"
              />
              {children}
            </main>
          </AuthorizationContext>
        </body>
      </html>
    </StoreProvider>
  );
}
