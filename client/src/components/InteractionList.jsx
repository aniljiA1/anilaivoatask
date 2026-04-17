import { useSelector } from "react-redux";

export default function InteractionList() {
  const interactions = useSelector((state) => state.interactions.list);

  return (
    <div>
      <h3 className="text-xl font-semibold mb-3">Interaction List</h3>

      {interactions.length === 0 ? (
        <p className="text-gray-500">No interactions yet</p>
      ) : (
        interactions.map((item) => (
          <div key={item.id} className="border p-3 rounded-lg mb-2 bg-gray-50">
            <p className="font-medium">Doctor: {item.doctor}</p>
            <p className="text-sm text-gray-600">{item.notes}</p>
          </div>
        ))
      )}
    </div>
  );
}
