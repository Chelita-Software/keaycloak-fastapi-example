import { createAppSlice } from "@/lib/createAppSlice";

export interface DummieSliceState {
  value: boolean;
}

const initialState: DummieSliceState = {
  value: false,
};

export const dummieSlice = createAppSlice({
  name: "dummie",
  // `createSlice` will infer the state type from the `initialState` argument
  initialState,
  reducers: {}, 
});