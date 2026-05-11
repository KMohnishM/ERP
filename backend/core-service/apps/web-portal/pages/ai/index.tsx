
import React from "react";
import Sidebar from "@/components/layout/Sidebar";

export default function AIServicePage() {
  return (
    <div className="flex bg-slate-50 min-h-screen">
      <Sidebar />
      <main className="ml-64 p-8 w-full">
        <header className="mb-8">
          <h1 className="text-3xl font-bold text-slate-900">AI Insights</h1>
          <p className="text-slate-500">Predictive analytics and workflow automation</p>
        </header>
        <div className="bg-white rounded-xl shadow-sm border border-slate-200 p-8 text-center py-12">
          <div className="mb-4 inline-flex items-center justify-center w-12 h-12 rounded-full bg-blue-100 text-blue-600">
            <span className="text-2xl font-bold">?</span>
          </div>
          <p className="text-slate-600">The AI Service is analyzing your system data...</p>
        </div>
      </main>
    </div>
  );
}
