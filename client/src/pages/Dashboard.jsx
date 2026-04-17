import ChatInterface from "../components/ChatInterface";
import InteractionForm from "../components/InteractionForm";
import InteractionList from "../components/InteractionList";

export default function Dashboard() {
  return (
    <div className="min-h-screen bg-gray-100 p-6 font-sans">
      <h1 className="text-3xl font-bold text-center mb-6">
        AI CRM - HCP Interaction
      </h1>

      <div className="grid md:grid-cols-2 gap-6">
        {/* LEFT */}
        <div className="bg-white p-5 rounded-2xl shadow">
          <InteractionForm />
          <InteractionList />
        </div>

        {/* RIGHT */}
        <div className="bg-white p-5 rounded-2xl shadow">
          <ChatInterface />
        </div>
      </div>
    </div>
  );
}
