import {
    LayoutDashboard,
    MessageSquare,
    Ticket,
    BookOpen,
    BarChart3,
    Settings
} from "lucide-react";

import { NavLink } from "react-router-dom";

import Logo from "./Logo";

const items = [
    {
        name: "Dashboard",
        icon: LayoutDashboard,
        path: "/"
    },
    {
        name: "AI Chat",
        icon: MessageSquare,
        path: "/chat"
    },
    {
        name: "Tickets",
        icon: Ticket,
        path: "/tickets"
    },
    {
        name: "Knowledge",
        icon: BookOpen,
        path: "/knowledge"
    },
    {
        name: "Analytics",
        icon: BarChart3,
        path: "/analytics"
    },
    {
        name: "Settings",
        icon: Settings,
        path: "/settings"
    }
];

export default function Sidebar() {
    return (
        <aside className="w-64 bg-slate-900 border-r border-slate-800 min-h-screen">

            <Logo />

            <nav className="mt-8 flex flex-col gap-2 px-3">

                {items.map((item) => (
                    <NavLink
                        key={item.path}
                        to={item.path}
                        className="flex items-center gap-3 rounded-lg px-4 py-3 text-slate-300 hover:bg-slate-800 transition"
                    >
                        <item.icon size={20} />

                        {item.name}
                    </NavLink>
                ))}

            </nav>

        </aside>
    );
}