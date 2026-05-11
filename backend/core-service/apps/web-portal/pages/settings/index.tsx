
import React from "react";
import Sidebar from "@/components/layout/Sidebar";
import { Settings2, Bell, Shield, Cloud, Database, Cpu } from "lucide-react";

export default function SettingsPage() {
  return (
    <div className="flex bg-slate-50 min-h-screen">
      <Sidebar />
      <main className="ml-64 p-8 w-full">
        <header className="mb-8">
          <h1 className="text-3xl font-black text-slate-900 tracking-tight">System Configuration</h1>
          <p className="text-slate-500 font-medium">Global environment variables, security protocols, and integration keys</p>
        </header>

        <div className="max-w-4xl space-y-6">
           {[
             { title: "Enterprise Settings", desc: "Corporate identity, multi-tenant branding, and locale", icon: Settings2 },
             { title: "Notification Engine", desc: "SMTP configuration, Slack hooks, and real-time alerts", icon: Bell },
             { title: "Security & IAM", desc: "Two-factor authentication, OAuth providers, and API keys", icon: Shield },
             { title: "Infrastructure", desc: "Kubernetes scaling parameters, CDN nodes, and S3 paths", icon: Cloud },
             { title: "Database & Backups", desc: "PostgreSQL maintenance, WAL replication, and cold storage", icon: Database },
             { title: "AI Tuning", desc: "LLM parameter selection, context windows, and token limits", icon: Cpu }
           ].map((opt, i) => (
             <div key={i} className="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm flex items-center justify-between hover:bg-slate-50 transition-colors cursor-pointer group">
                <div className="flex items-center space-x-6">
                   <div className="w-12 h-12 bg-slate-100 rounded-xl flex items-center justify-center text-slate-600 group-hover:bg-blue-600 group-hover:text-white transition-all">
                      <opt.icon size={22} />
                   </div>
                   <div>
                      <h4 className="font-black text-slate-900 tracking-tight">{opt.title}</h4>
                      <p className="text-sm text-slate-500">{opt.desc}</p>
                   </div>
                </div>
                <button className="text-[10px] font-black uppercase tracking-widest text-blue-600 px-4 py-2 bg-blue-50 rounded-lg group-hover:bg-blue-600 group-hover:text-white transition-all">Configure</button>
             </div>
           ))}
        </div>
      </main>
    </div>
  );
}
