
import React from "react";
import Sidebar from "@/components/layout/Sidebar";
import { BrainCircuit, Sparkles, Wand2, Zap, MessageSquare } from "lucide-react";

export default function AIServicePage() {
  return (
    <div className="flex bg-slate-50 min-h-screen">
      <Sidebar />
      <main className="ml-64 p-8 w-full">
        <header className="mb-8">
          <div className="flex items-center space-x-3 mb-2">
            <div className="w-10 h-10 bg-purple-600 rounded-xl flex items-center justify-center shadow-lg shadow-purple-200">
               <BrainCircuit className="text-white" size={24} />
            </div>
            <h1 className="text-3xl font-black text-slate-900 tracking-tight">AI Intelligence Layer</h1>
          </div>
          <p className="text-slate-500 font-medium">Predictive modeling and automated decision support systems</p>
        </header>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8 mb-8">
           <div className="lg:col-span-2 space-y-8">
              <div className="bg-white p-8 rounded-2xl border border-slate-200 shadow-sm relative overflow-hidden group">
                 <div className="absolute top-0 right-0 p-4 opacity-5 group-hover:opacity-10 transition-opacity">
                    <Sparkles size={120} />
                 </div>
                 <h2 className="text-xl font-black text-slate-800 mb-2">Smart Forecast Engine</h2>
                 <p className="text-slate-500 mb-6 max-w-md">Our neural network is analyzing 12.4M data points from your Finance and Supply Chain logs to generate next month projections.</p>
                 <div className="flex space-x-4">
                    <button className="bg-purple-600 text-white px-6 py-3 rounded-xl font-bold flex items-center hover:bg-purple-700 shadow-xl transition-all active:scale-95">
                       <Zap size={18} className="mr-2" /> Run New Prediction
                    </button>
                    <button className="px-6 py-3 rounded-xl font-bold text-slate-600 hover:bg-slate-50 transition-colors border border-slate-200">
                       View Training Logs
                    </button>
                 </div>
              </div>

              <div className="bg-slate-900 rounded-2xl p-8 text-white shadow-2xl">
                 <div className="flex items-center space-x-2 text-purple-400 mb-4">
                    <MessageSquare size={20} />
                    <span className="font-bold text-xs uppercase tracking-widest">Enterprise Assistant</span>
                 </div>
                 <div className="h-48 flex flex-col justify-end">
                    <div className="bg-white/10 p-4 rounded-xl backdrop-blur-sm self-start mb-4 max-w-sm">
                       <p className="text-sm">\"Based on your current stock burn rate, I recommend ordering 50 units of Titanium Rods immediately to avoid production downtime.\"</p>
                    </div>
                    <div className="flex bg-white/5 rounded-2xl border border-white/10 p-2 items-center">
                       <input type="text" placeholder="Ask anything about your business data..." className="bg-transparent flex-1 px-4 text-sm outline-none" />
                       <button className="bg-purple-500 p-2 rounded-xl hover:bg-purple-400"><Wand2 size={18} /></button>
                    </div>
                 </div>
              </div>
           </div>

           <div className="space-y-6">
              <h3 className="font-black text-xs text-slate-400 uppercase tracking-[0.2em]">Active AI Agents</h3>
              {[
                { name: "Cost Optimizer", status: "Active", efficiency: "+22%", icon: Zap },
                { name: "Anomaly Detector", status: "Listening", efficiency: "100%", icon: Sparkles },
                { name: "Risk Assessment", status: "Active", efficiency: "98.4%", icon: BrainCircuit }
              ].map((agent, i) => (
                <div key={i} className="bg-white p-6 rounded-2xl border border-slate-200 flex items-center justify-between shadow-sm">
                   <div className="flex items-center space-x-4">
                      <div className="w-12 h-12 bg-slate-50 rounded-xl flex items-center justify-center text-purple-600">
                         <agent.icon size={20} />
                      </div>
                      <div>
                         <p className="font-black text-slate-800 text-sm">{agent.name}</p>
                         <p className="text-[10px] text-emerald-500 font-bold uppercase tracking-widest">{agent.status}</p>
                      </div>
                   </div>
                   <span className="text-lg font-black text-slate-900">{agent.efficiency}</span>
                </div>
              ))}
           </div>
        </div>
      </main>
    </div>
  );
}
