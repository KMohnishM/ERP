
import React from "react";
import Sidebar from "@/components/layout/Sidebar";
import { Workflow, MapPin, Building2, ShieldCheck, Fingerprint } from "lucide-react";

export default function OrgPage() {
  const departments = [
    { id: 1, name: "Engineering", head: "Dr. Aris V.", staff: 42, color: "bg-blue-500" },
    { id: 2, name: "Financial Ops", head: "Sarah Chen", staff: 18, color: "bg-emerald-500" },
    { id: 3, name: "Global Logistics", head: "Marco Rossi", staff: 35, color: "bg-amber-500" },
    { id: 4, name: "Human Capital", head: "Elena G.", staff: 12, color: "bg-purple-500" },
  ];

  return (
    <div className="flex bg-slate-50 min-h-screen">
      <Sidebar />
      <main className="ml-64 p-8 w-full">
        <header className="mb-8">
          <h1 className="text-3xl font-black text-slate-900 tracking-tight">Organization & Hierarchy</h1>
          <p className="text-slate-500 font-medium">Enterprise structure, department management, and legal entities</p>
        </header>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-8">
          <div className="bg-white rounded-2xl p-8 border border-slate-200 shadow-sm">
             <div className="flex items-center space-x-3 mb-6">
                <Building2 className="text-blue-600" />
                <h2 className="text-xl font-bold text-slate-800">Legal Entity Details</h2>
             </div>
             <div className="space-y-4">
                <div className="flex justify-between border-b border-slate-50 pb-3">
                   <span className="text-slate-400 font-bold text-xs uppercase tracking-widest">Register Name</span>
                   <span className="text-slate-900 font-black">ERP CORE ENTERPRISE LTD</span>
                </div>
                <div className="flex justify-between border-b border-slate-50 pb-3">
                   <span className="text-slate-400 font-bold text-xs uppercase tracking-widest">Tax ID (VAT)</span>
                   <span className="text-slate-900 font-black font-mono">GB-990-112-X</span>
                </div>
                <div className="flex justify-between border-b border-slate-50 pb-3">
                   <span className="text-slate-400 font-bold text-xs uppercase tracking-widest">HQ Location</span>
                   <span className="text-slate-900 font-black">London, United Kingdom</span>
                </div>
             </div>
          </div>

          <div className="bg-gradient-to-br from-slate-800 to-slate-900 rounded-2xl p-8 text-white shadow-xl relative overflow-hidden">
             <Fingerprint className="absolute -bottom-4 -right-4 text-white/10" size={120} />
             <div className="flex items-center space-x-3 mb-6">
                <ShieldCheck className="text-emerald-400" />
                <h2 className="text-xl font-bold">Security & Compliance</h2>
             </div>
             <p className="text-slate-400 mb-6 text-sm">Your organization is currently running on **Schema Isolation (Postgres)** with full audit logging enabled.</p>
             <div className="grid grid-cols-2 gap-4">
                <div className="bg-white/5 p-4 rounded-xl border border-white/10">
                   <p className="text-[10px] uppercase font-black tracking-widest opacity-50">Data Residency</p>
                   <p className="font-bold">EU-WEST-1</p>
                </div>
                <div className="bg-white/5 p-4 rounded-xl border border-white/10">
                   <p className="text-[10px] uppercase font-black tracking-widest opacity-50">Encryption</p>
                   <p className="font-bold text-emerald-400">AES-256</p>
                </div>
             </div>
          </div>
        </div>

        <h3 className="font-black text-xs text-slate-400 uppercase tracking-[0.2em] mb-6">Departments & Divisions</h3>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
           {departments.map(dept => (
             <div key={dept.id} className="bg-white rounded-2xl p-6 border border-slate-200 shadow-sm hover:ring-2 hover:ring-blue-100 transition-all cursor-pointer group">
                <div className={`${dept.color} w-10 h-1 h-2 rounded-full mb-4`}></div>
                <h4 className="font-black text-slate-900 mb-1 group-hover:text-blue-600 transition-colors uppercase text-sm tracking-tight">{dept.name}</h4>
                <p className="text-xs text-slate-500 font-medium mb-4">Lead: {dept.head}</p>
                <div className="flex items-center justify-between">
                   <div className="flex items-center -space-x-2">
                       {[1,2,3].map(i => <div key={i} className="w-6 h-6 rounded-full bg-slate-100 border-2 border-white"></div>)}
                       <span className="text-[10px] pl-3 font-bold text-slate-400">+{dept.staff} more</span>
                   </div>
                   <Workflow size={16} className="text-slate-200 group-hover:text-blue-400 transition-colors" />
                </div>
             </div>
           ))}
        </div>
      </main>
    </div>
  );
}
