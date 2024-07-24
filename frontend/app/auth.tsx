"use client";
import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import type { ReactNode } from "react";

import { useAppDispatch, useAppSelector } from "@/lib/hooks";
import { verifyAuth } from "@/lib/features/auth/authSlice";

interface Props {
    readonly children: ReactNode;
}

export default function AuthorizationContext({ children }: Props) {
    const dispatch = useAppDispatch();
    const router = useRouter();
    const { isAuthenticated } = useAppSelector((state) => state.auth);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        dispatch(verifyAuth({}))
    }, []);

    useEffect(() => {
        if (isAuthenticated === null) {
          return;
        }
        if (isAuthenticated === false && window.location.pathname !== "/login") {
          router.push("/login")
        } 
        setLoading(false);
      }, [isAuthenticated]);

    return loading ? <p>Loading...</p> : children;
}