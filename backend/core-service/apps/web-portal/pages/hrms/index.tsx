
import React from "react";
import Sidebar from "@/components/layout/Sidebar";
import { useEmployees } from "@/lib/hooks/use-employees";
import { Plus, UserCheck, Timer, CreditCard } from "lucide-react";

export default function HRMSPage() {
  const { data: employees, isLoading } = useEmployees();

  return (
    <div className="flex bg-slate-50 min-h-screen">
      <Sidebar />
      <main className="ml-64 p-8 w-full">
        <header className="flex justify-between items-center mb-8">
          <div>
            <h1 className="text-3xl font-bold text-slate-900 tracking-tight">Human Resources</h1>
            <p className="text-slate-500 font-medium">Manage workforce, payroll, and performance</p>
          </div>
          <button className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-lg font-bold flex items-center shadow-lg transition-all active:scale-95">
            <Plus size={20} className="mr-2" /> Add Employee
          </button>
        </header>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
          <div className="bg-white p-6 rounded-xl shadow-sm border border-slate-200">
            <div className="flex items-center text-blue-600 mb-2">
              <UserCheck size={20} className="mr-2" />
              <span className="font-bold uppercase text-xs tracking-wider">Active Staff</span>
            </div>
            <p className="text-3xl font-black text-slate-900">{isLoading ? "..." : employees?.length || 0}</p>
          </div>
          <div className="bg-white p-6 rounded-xl shadow-sm border border-slate-200">
            <div className="flex items-center text-emerald-600 mb-2">
              <Timer size={20} className="mr-2" />
              <span className="font-bold uppercase text-xs tracking-wider">On Leave</span>
            </div>
            <p className="text-3xl font-black text-slate-900">12</p>
          </div>
          <div className="bg-white p-6 rounded-xl shadow-sm border border-slate-200">
            <div className="flex items-center text-purple-600 mb-2">
              <CreditCard size={20} className="mr-2" />
              <span className="font-bold uppercase text-xs tracking-wider">Next Payroll</span>
            </div>
            <p className="text-3xl font-black text-slate-900">May 30</p>
          </div>
        </div>

        <div className="bg-white rounded-xl shadow-sm border border-slate-200 overflow-hidden">
          <div className="p-6 border-b border-slate-100 flex justify-between items-center bg-slate-50/50">
            <h2 className="font-bold text-slate-800">Employee Directory</h2>
          </div>
          <table className="w-full text-left border-collapse">
            <thead>
              <tr className="bg-slate-50 text-slate-500 text-xs font-bold uppercase tracking-widest border-b border-slate-100">
                <th className="px-6 py-4">Name</th>
                <th className="px-6 py-4">Department</th>
                <th className="px-6 py-4">Status</th>
                <th className="px-6 py-4">Join Date</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-50 text-slate-600">
              {isLoading ? (
                <tr><td colSpan={4} className="px-6 py-8 text-center animate-pulse">Loading employee data...</td></tr>
              ) : employees?.map((emp: any) => (
                <tr key={emp.id} className="hover:bg-slate-50 transition-colors">
                  <td className="px-6 py-4 font-bold text-slate-800">{emp.first_name} {emp.last_name}</td>
                  <td className="px-6 py-4">{emp.department || "General"}</td>
                  <td className="px-6 py-4">
                    <span className="px-2 py-1 bg-emerald-100 text-emerald-700 text-[10px] font-black rounded uppercase">Active</span>
                  </td>
                  <td className="px-6 py-4 font-mono text-sm">{new Date().toLocaleDateString()}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </main>
    </div>
  );
}
