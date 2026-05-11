
import React from "react";
import Sidebar from "@/components/layout/Sidebar";
import { TrendingUp, TrendingDown, Landmark, FileSpreadsheet } from "lucide-react";

export default function FinancePage() {
  return (
    <div className="flex bg-slate-50 min-h-screen">
      <Sidebar />
      <main className="ml-64 p-8 w-full">
        <header className="mb-8">
          <h1 className="text-3xl font-bold text-slate-900 tracking-tight">Finance & Ledger</h1>
          <p className="text-slate-500 font-medium">Double-entry accounting and asset management</p>
        </header>

        <div className="grid grid-cols-1 lg:grid-cols-4 gap-6 mb-8">
          <div className="bg-gradient-to-br from-blue-600 to-blue-700 p-6 rounded-2xl shadow-xl text-white col-span-2">
            <div className="flex justify-between items-start mb-4">
              <Landmark size={24} className="opacity-80" />
              <span className="text-[10px] bg-white/20 px-2 py-1 rounded-full font-bold uppercase tracking-widest">Main Account</span>
            </div>
            <p className="text-sm font-medium opacity-80 uppercase tracking-wider mb-1">Total Liquidity</p>
            <p className="text-4xl font-black">$2,450,890.00</p>
          </div>
          <div className="bg-white p-6 rounded-2xl shadow-sm border border-slate-200">
            <TrendingUp size={24} className="text-emerald-500 mb-4" />
            <p className="text-xs font-bold text-slate-400 uppercase tracking-widest mb-1">Revenue (MoM)</p>
            <p className="text-2xl font-black text-slate-900">+14.2%</p>
          </div>
          <div className="bg-white p-6 rounded-2xl shadow-sm border border-slate-200">
            <TrendingDown size={24} className="text-rose-500 mb-4" />
            <p className="text-xs font-bold text-slate-400 uppercase tracking-widest mb-1">Expenses (MoM)</p>
            <p className="text-2xl font-black text-slate-900">-4.8%</p>
          </div>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          <div className="lg:col-span-2 bg-white rounded-xl shadow-sm border border-slate-200 p-6">
            <div className="flex justify-between items-center mb-6">
              <h2 className="font-bold text-slate-800 tracking-tight">Recent Transactions</h2>
              <button className="text-blue-600 text-xs font-bold hover:underline">View All Ledger</button>
            </div>
            <div className="space-y-4">
              {[1,2,3,4].map(idx => (
                <div key={idx} className="flex items-center justify-between p-4 bg-slate-50 rounded-xl hover:shadow-inner transition-all border border-transparent hover:border-slate-200">
                  <div className="flex items-center space-x-4">
                    <div className="w-10 h-10 rounded-full bg-white flex items-center justify-center shadow-sm">
                      <FileSpreadsheet size={18} className="text-slate-400" />
                    </div>
                    <div>
                      <p className="font-bold text-slate-800">Office Maintenance Vendor</p>
                      <p className="text-[10px] text-slate-400 font-bold uppercase tracking-tighter">Debit • Operations</p>
                    </div>
                  </div>
                  <p className="font-black text-slate-900">-$450.00</p>
                </div>
              ))}
            </div>
          </div>
          <div className="bg-white rounded-xl shadow-sm border border-slate-200 p-6">
            <h2 className="font-bold text-slate-800 mb-6">Tax Liability (Q2)</h2>
            <div className="space-y-6">
              <div className="relative pt-1">
                <div className="flex mb-2 items-center justify-between">
                  <span className="text-xs font-bold uppercase text-slate-500">VAT Collected</span>
                  <span className="text-xs font-black text-slate-900">$12,400</span>
                </div>
                <div className="overflow-hidden h-2 text-xs flex rounded bg-slate-100">
                  <div style={{ width: "65%" }} className="shadow-none flex flex-col text-center whitespace-nowrap text-white justify-center bg-blue-500"></div>
                </div>
              </div>
              <div className="relative pt-1">
                <div className="flex mb-2 items-center justify-between">
                  <span className="text-xs font-bold uppercase text-slate-500">Corporate Tax</span>
                  <span className="text-xs font-black text-slate-900">$45,000</span>
                </div>
                <div className="overflow-hidden h-2 text-xs flex rounded bg-slate-100">
                  <div style={{ width: "30%" }} className="shadow-none flex flex-col text-center whitespace-nowrap text-white justify-center bg-purple-500"></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}
