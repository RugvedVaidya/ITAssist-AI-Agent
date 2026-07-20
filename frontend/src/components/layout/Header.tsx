export default function Header() {
    return (
        <header className="h-16 border-b border-slate-800 bg-slate-950 flex items-center justify-between px-8">

            <h2 className="text-xl font-semibold">
                Dashboard
            </h2>

            <div className="flex items-center gap-4">

                <div className="h-10 w-10 rounded-full bg-blue-600" />

            </div>

        </header>
    );
}