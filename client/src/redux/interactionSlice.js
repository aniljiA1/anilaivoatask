import { createSlice } from "@reduxjs/toolkit";

const interactionSlice = createSlice({
  name: "interactions",
  initialState: {
    list: [],
  },
  reducers: {
    addInteraction: (state, action) => {
      state.list.push(action.payload);
    },
    updateInteraction: (state, action) => {
      const index = state.list.findIndex(
        (item) => item.id === action.payload.id,
      );
      if (index !== -1) {
        state.list[index] = action.payload;
      }
    },
  },
});

export const { addInteraction, updateInteraction } = interactionSlice.actions;
export default interactionSlice.reducer;
