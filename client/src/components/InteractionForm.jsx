import { useState } from "react";
import { useDispatch } from "react-redux";
import { addInteraction } from "../redux/interactionSlice";
import axios from "axios";

export default function InteractionForm() {
  const dispatch = useDispatch();

  const [form, setForm] = useState({
    doctor: "",
    notes: "",
  });

  const handleSubmit = async () => {
    if (!form.doctor || !form.notes) return;

    try {
      await axios.post(`${import.meta.env.VITE_API_URL}/log`, form);

      dispatch(
        addInteraction({
          id: Date.now(),
          ...form,
        }),
      );

      setForm({ doctor: "", notes: "" });
    } catch (err) {
      console.error(err);
      alert("Error logging interaction");
    }
  };

  return (
    <div className="mb-6">
      <h3 className="text-xl font-semibold mb-3">Log Interaction</h3>

      <input
        className="w-full p-2 border rounded-lg mb-3"
        placeholder="Doctor Name"
        value={form.doctor}
        onChange={(e) => setForm({ ...form, doctor: e.target.value })}
      />

      <textarea
        className="w-full p-2 border rounded-lg mb-3"
        placeholder="Notes"
        value={form.notes}
        onChange={(e) => setForm({ ...form, notes: e.target.value })}
      />

      <button
        onClick={handleSubmit}
        className="w-full bg-blue-500 text-white py-2 rounded-lg hover:bg-blue-600"
      >
        Submit
      </button>
    </div>
  );
}
