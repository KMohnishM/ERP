import React from 'react';
import Link from 'next/link';
import { 
  LayoutDashboard, 
  Users, 
  Wallet, 
  Package, 
  FileText, 
  Settings,
  BrainCircuit,
  Workflow
} from 'lucide-react';

const Sidebar = () => {
  const menuItems = [
    { name: 'Dashboard', icon: LayoutDashboard, href: '/' },
    { name: 'Organization', icon: Workflow, href: '/org' },
    { name: 'HR & Payroll', icon: Users, href: '/hrms' },
    { name: 'Finance', icon: Wallet, href: '/finance' },
    { name: 'Inventory', icon: Package, href: '/inventory' },
    { name: 'AI Insights', icon: BrainCircuit, href: '/ai' },
    { name: 'Settings', icon: Settings, href: '/settings' },
  ];

  return (
    <div className="w-64 h-screen bg-slate-900 text-white fixed left-0 top-0 p-4 border-r border-slate-800">
      <div className="mb-8 px-2 flex items-center space-x-2">
        <div className="w-8 h-8 bg-blue-600 rounded-lg flex items-center justify-center font-bold">E</div>
        <h1 className="text-xl font-bold tracking-tight">ERP CORE</h1>
      </div>
      <nav className="space-y-1">
        {menuItems.map((item) => (
          <Link 
            key={item.name} 
            href={item.href}
            className="flex items-center space-x-3 px-3 py-2 rounded-lg hover:bg-slate-800 transition-colors text-slate-300 hover:text-white group"
          >
            <item.icon size={20} className="group-hover:text-blue-400" />
            <span className="font-medium">{item.name}</span>
          </Link>
        ))}
      </nav>
    </div>
  );
};

export default Sidebar;
