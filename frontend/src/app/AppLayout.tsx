import { Outlet } from "react-router-dom";
import Sidebar from "@/components/layout/Sidebar";
import Header from "@/components/layout/Header";

export default function AppLayout() {
    return (
        <div className="flex min-h-screen bg-slate-950 text-white">

            <Sidebar />

            <div className="flex flex-col flex-1">

                <Header />

                <main className="p-8">
                    <Outlet />
                </main>

            </div>

        </div>
    );
}