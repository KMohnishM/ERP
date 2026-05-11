
import React from "react";
import Sidebar from "@/components/layout/Sidebar";
import { Package, AlertTriangle, ArrowDownCircle, ArrowUpCircle, Search } from "lucide-react";

export default function InventoryPage() {
  const stockItems = [
    { id: 1, name: "Precision Lathe Model X", sku: "IND-882-QX", stock: 12, minStock: 5, status: "Healthy" },
    { id: 2, name: "Industrial Grade Lubricant", sku: "CHEM-441-A", stock: 150, minStock: 200, status: "Low Stock" },
    { id: 3, name: "Titanium Alloy Rods", sku: "MET-001-B", stock: 0, minStock: 10, status: "Out of Stock" },
  ];

  return (
    <div className="flex bg-slate-50 min-h-screen">
      <Sidebar />
      <main className="ml-64 p-8 w-full">
        <header className="flex justify-between items-center mb-8">
          <div>
            <h1 className="text-3xl font-bold text-slate-900 tracking-tight">Supply Chain & Inventory</h1>
            <p className="text-slate-500 font-medium">Global warehouse tracking and replenishment logic</p>
          </div>
          <div className="flex space-x-3">
            <button className="bg-slate-900 text-white px-4 py-2 rounded-lg font-bold flex items-center hover:bg-slate-800 transition-all">
              <ArrowDownCircle size={18} className="mr-2" /> Stock In
            </button>
            <button className="bg-blue-600 text-white px-4 py-2 rounded-lg font-bold flex items-center hover:bg-blue-700 shadow-lg transition-all">
              <Package size={18} className="mr-2" /> Add SKU
            </button>
          </div>
        </header>

        <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
          {[
            { label: "Total SKUs", val: "1,240", icon: Package, color: "text-blue-600" },
            { label: "Low Stock Alert", val: "14", icon: AlertTriangle, color: "text-amber-500" },
            { label: "Out of Stock", val: "3", icon: AlertTriangle, color: "text-rose-600" },
            { label: "Warehouse Capacity", val: "78%", icon: ArrowUpCircle, color: "text-emerald-600" },
          ].map((stat, i) => (
            <div key={i} className="bg-white p-6 rounded-xl border border-slate-200 shadow-sm">
              <stat.icon size={20} className={`${stat.color} mb-3`} />
              <p className="text-xs font-bold text-slate-400 uppercase tracking-widest">{stat.label}</p>
              <p className="text-2xl font-black text-slate-900">{stat.val}</p>
            </div>
          ))}
        </div>

        <div className="bg-white rounded-2xl shadow-sm border border-slate-200">
          <div className="p-4 border-b border-slate-100 flex items-center bg-slate-50/30">
             <div className="relative flex-1 max-w-md">
                <Search size={18} className="absolute left-3 top-1/2 transform -translate-y-1/2 text-slate-400" />
                <input type="text" placeholder="Search inventory by SKU or Name..." className="w-full pl-10 pr-4 py-2 bg-white border border-slate-200 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 outline-none" />
             </div>
          </div>
          <table className="w-full text-left">
            <thead>
              <tr className="border-b border-slate-50 text-[10px] font-black text-slate-400 uppercase tracking-widest bg-slate-50/50">
                <th className="px-6 py-4">Item Details</th>
                <th className="px-6 py-4">SKU / ID</th>
                <th className="px-6 py-4">Availability</th>
                <th className="px-6 py-4">Status</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-50">
              {stockItems.map(item => (
                <tr key={item.id} className="hover:bg-slate-50 transition-colors">
                  <td className="px-6 py-4">
                    <p className="font-bold text-slate-800">{item.name}</p>
                  </td>
                  <td className="px-6 py-4 font-mono text-xs text-slate-500">{item.sku}</td>
                  <td className="px-6 py-4">
                    <div className="flex items-center space-x-2">
                       <span className="font-black text-slate-900">{item.stock}</span>
                       <span className="text-slate-300">/</span>
                       <span className="text-slate-400 text-xs font-bold">{item.minStock} min</span>
                    </div>
                  </td>
                  <td className="px-6 py-4">
                    <span className={`px-2 py-1 rounded-full text-[10px] font-black uppercase ${
                      item.status === "Healthy" ? "bg-emerald-100 text-emerald-700" :
                      item.status === "Low Stock" ? "bg-amber-100 text-amber-700" :
                      "bg-rose-100 text-rose-700"
                    }`}>
                      {item.status}
                    </span>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </main>
    </div>
  );
}
