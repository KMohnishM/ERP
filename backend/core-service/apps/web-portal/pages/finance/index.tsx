
import React from "react";
import Sidebar from "@/components/layout/Sidebar";

export default function FinancePage() {
  return (
    <div className="flex bg-slate-50 min-h-screen">
      <Sidebar />
      <main className="ml-64 p-8 w-full">
        <header className="mb-8">
          <h1 className="text-3xl font-bold text-slate-900">Finance & Accounting</h1>
          <p className="text-slate-500">General ledger, accounts payable, and accounts receivable</p>
        </header>
        <div className="bg-white rounded-xl shadow-sm border border-slate-200 p-8">
          <p className="text-slate-600">Financial statements and ledger tools coming soon.</p>
        </div>
      </main>
    </div>
  );
}
