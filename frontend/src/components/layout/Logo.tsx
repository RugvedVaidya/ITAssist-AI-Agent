export default function Logo() {
    return (
        <div className="flex items-center gap-3 px-4 py-5">
            <div className="h-10 w-10 rounded-xl bg-blue-600 flex items-center justify-center font-bold text-white">
                AI
            </div>

            <div>
                <h1 className="font-bold text-lg">
                    ITAssist
                </h1>

                <p className="text-xs text-slate-400">
                    Enterprise AI
                </p>
            </div>
        </div>
    );
}