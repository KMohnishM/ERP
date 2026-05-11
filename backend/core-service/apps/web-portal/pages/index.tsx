import React from '\''react'\'';
import Sidebar from '\''@/components/layout/Sidebar'\'';

const IndexPage = () => {
  return (
    <div className="flex bg-slate-50 min-h-screen">
      <Sidebar />
      <main className="ml-64 p-8 w-full">
        <header className="mb-8">
          <h1 className="text-3xl font-bold text-slate-900 leading-tight">Enterprise Dashboard</h1>
          <p className="text-slate-500">Overview of your modular ERP platform status</p>
        </header>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
          {[
            { label: '\''Total Revenue'\'', value: '\''$124,500'\'', color: '\''border-blue-500'\'' },
            { label: '\''Active Employees'\'', value: '\''430'\'', color: '\''border-emerald-500'\'' },
            { label: '\''Stock Alerts'\'', value: '\''12 Items'\'', color: '\''border-amber-500'\'' },
            { label: '\''AI Recommendations'\'', value: '\''5 New'\'', color: '\''border-purple-500'\'' },
          ].map((stat) => (
            <div key={stat.label} className={`bg-white p-6 rounded-xl shadow-sm border-l-4 ${stat.color} hover:shadow-md transition-shadow`}>
              <p className="text-sm font-medium text-slate-500 uppercase tracking-wider">{stat.label}</p>
              <p className="text-2xl font-bold text-slate-900 mt-2">{stat.value}</p>
            </div>
          ))}
        </div>

        <section className="bg-white rounded-xl shadow-sm border border-slate-200 p-8">
          <h2 className="text-xl font-bold text-slate-900 mb-4">Core System Status</h2>
          <div className="space-y-4">
            <div className="flex items-center justify-between p-4 bg-slate-50 rounded-lg">
              <span className="font-medium">Multi-Tenant Backend</span>
              <span className="px-2 py-1 bg-emerald-100 text-emerald-700 text-xs font-bold rounded">OPERATIONAL</span>
            </div>
            <div className="flex items-center justify-between p-4 bg-slate-50 rounded-lg">
              <span className="font-medium">Workflow Engine</span>
              <span className="px-2 py-1 bg-emerald-100 text-emerald-700 text-xs font-bold rounded">OPERATIONAL</span>
            </div>
            <div className="flex items-center justify-between p-4 bg-slate-50 rounded-lg">
              <span className="font-medium">AI Service Layer</span>
              <span className="px-2 py-1 bg-blue-100 text-blue-700 text-xs font-bold rounded">CONNECTED</span>
            </div>
          </div>
        </section>
      </main>
    </div>
  );
};

export default IndexPage;
