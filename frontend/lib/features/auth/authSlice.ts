import { createAppSlice } from "@/lib/createAppSlice";
import { callVerifyAuth } from "./authAPI";

export interface DummieSliceState {
  isAuthenticated: boolean | null;
  loading: boolean;
}

const initialState: DummieSliceState = {
  isAuthenticated: null,
  loading: false,
};

export const authSlice = createAppSlice({
  name: "auth",
  initialState,
  reducers: (create) => ({
    verifyAuth: create.asyncThunk(
      async (payload: any) => {
        const response = await callVerifyAuth();
        return response;
      },
      {
        pending: (state) => {
          console.log("Calling verify auth");
          state.loading = true;
        },
        fulfilled: (state, action) => {
          console.log("Auth verified");
          state.loading = false;
          state.isAuthenticated = true;
        },
        rejected: (state, action) => {
          console.log("Failed to verify auth");
          state.isAuthenticated = false;
        },
      }
    ),
  }),
});

export const { verifyAuth } = authSlice.actions;