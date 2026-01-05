
import React from 'react';
import { Layers, ShoppingBag, Megaphone, Code, CheckCircle, Plus } from 'lucide-react';

const IntegrationCard = ({ logo, name, status, type }) => (
    <div className="card hover:shadow-lg transition-all border border-slate-700 bg-slate-800/50">
        <div className="flex justify-between items-start mb-4">
            <div className="w-12 h-12 rounded-xl bg-white p-2 flex items-center justify-center">
                {/* Placeholder for logos since we don't have distinct image files yet. Using text fallback */}
                <span className="text-slate-900 font-bold text-xs text-center leading-tight">{logo}</span>
            </div>
            <div className={`px-2 py-1 rounded-full text-xs font-medium ${status === 'Active' ? 'bg-green-500/20 text-green-400' : 'bg-slate-600/30 text-slate-400'
                }`}>
                {status}
            </div>
        </div>
        <h3 className="text-white font-semibold mb-1">{name}</h3>
        <p className="text-slate-400 text-sm mb-4">{type}</p>
        <button className={`w-full py-2 rounded-lg text-sm font-medium transition-colors ${status === 'Active'
            ? 'bg-slate-700 text-white hover:bg-slate-600'
            : 'bg-indigo-600 text-white hover:bg-indigo-700'
            }`}>
            {status === 'Active' ? 'Configure' : 'Connect'}
        </button>
    </div>
);

const Integrations = () => {
    const integrations = [
        // App Development
        { name: 'iOS App', type: 'Native Mobile', status: 'Available', category: 'App Development', logo: 'iOS' },
        { name: 'Android App', type: 'Native Mobile', status: 'Available', category: 'App Development', logo: 'Android' },
        { name: 'React Native', type: 'Cross Platform', status: 'Active', category: 'App Development', logo: 'RN' },
        { name: 'Flutter', type: 'Cross Platform', status: 'Available', category: 'App Development', logo: 'Flutter' },

        // Development
        { name: 'SEMRush', type: 'SEO Tools', status: 'Active', category: 'Development', logo: 'SEO' },
        { name: 'Helium 10', type: 'Market Intelligence', status: 'Available', category: 'Development', logo: 'H10' },
        { name: 'JungleScout', type: 'Product Research', status: 'Available', category: 'Development', logo: 'JS' },

        // Marketplaces
        { name: 'Shopify', type: 'Sales Channel', status: 'Active', category: 'Marketplaces', logo: 'Shopify' },
        { name: 'Walmart', type: 'Marketplace', status: 'Available', category: 'Marketplaces', logo: 'Walmart' },
        { name: 'Amazon', type: 'Global Market', status: 'Pending', category: 'Marketplaces', logo: 'AWS' },
        { name: 'eBay', type: 'Auction Site', status: 'Available', category: 'Marketplaces', logo: 'eBay' },
        { name: 'Noon', type: 'Middle East', status: 'Available', category: 'Marketplaces', logo: 'Noon' },

        // Marketing
        { name: 'Meta Ads', type: 'Social Marketing', status: 'Active', category: 'Marketing', logo: 'Meta' },
        { name: 'Google Ads', type: 'Search Marketing', status: 'Available', category: 'Marketing', logo: 'G-Ads' },
        { name: 'TikTok', type: 'Video Ads', status: 'Available', category: 'Marketing', logo: 'TikTok' },
        { name: 'Snapchat', type: 'Social', status: 'Available', category: 'Marketing', logo: 'Snap' },
        { name: 'WhatsApp', type: 'Communication', status: 'Active', category: 'Marketing', logo: 'WA' },
    ];

    const categories = [
        { id: 'all', label: 'All Apps', icon: Layers },
        { id: 'App Development', label: 'App Development', icon: Code },
        { id: 'Marketplaces', label: 'Marketplaces', icon: ShoppingBag },
        { id: 'Marketing', label: 'Marketing', icon: Megaphone },
        { id: 'Development', label: 'Seller Tools', icon: Code },
    ];

    const [activeCategory, setActiveCategory] = React.useState('all');

    const filteredIntegrations = activeCategory === 'all'
        ? integrations
        : integrations.filter(i => i.category === activeCategory);

    return (
        <div className="p-6 animate-fade-in max-w-7xl mx-auto">
            <header className="mb-8">
                <h1 className="text-3xl font-bold text-white mb-2">Integration Ecosystem</h1>
                <p className="text-slate-400">Connect your store with top-tier tools for Growth, Sales, and Development.</p>
            </header>

            {/* Category Tabs */}
            <div className="flex gap-4 mb-8 overflow-x-auto pb-2">
                {categories.map(cat => (
                    <button
                        key={cat.id}
                        onClick={() => setActiveCategory(cat.id)}
                        className={`flex items-center gap-2 px-4 py-2 rounded-lg font-medium transition-all ${activeCategory === cat.id
                            ? 'bg-indigo-600 text-white shadow-lg shadow-indigo-500/25'
                            : 'bg-slate-800 text-slate-400 hover:bg-slate-700 hover:text-white'
                            }`}
                    >
                        <cat.icon size={18} />
                        {cat.label}
                    </button>
                ))}
            </div>

            {/* Grid */}
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
                {filteredIntegrations.map((integration, idx) => (
                    <IntegrationCard key={idx} {...integration} />
                ))}

                {/* Add New Card */}
                <div className="card border border-dashed border-slate-700 bg-slate-800/20 flex flex-col items-center justify-center min-h-[200px] hover:border-indigo-500 hover:bg-slate-800/30 transition-all cursor-pointer group">
                    <div className="w-12 h-12 rounded-full bg-slate-800 flex items-center justify-center mb-3 group-hover:bg-indigo-500/20 transition-colors">
                        <Plus className="text-slate-400 group-hover:text-indigo-400" />
                    </div>
                    <span className="text-slate-400 font-medium group-hover:text-white">Request Integration</span>
                </div>
            </div>

            <div className="mt-12 p-6 bg-gradient-to-r from-indigo-900/50 to-purple-900/50 rounded-2xl border border-indigo-500/30 flex items-center justify-between">
                <div>
                    <h3 className="text-xl font-bold text-white mb-1">Need a custom integration?</h3>
                    <p className="text-indigo-200">Our team can build bespoke connections for your enterprise needs.</p>
                </div>
                <button className="px-6 py-2 bg-white text-indigo-900 font-bold rounded-lg hover:bg-indigo-50 transition-colors">
                    Contact Sales
                </button>
            </div>
        </div>
    );
};

export default Integrations;
