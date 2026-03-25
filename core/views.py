from django.shortcuts import render, redirect


def home(request):
    services = [
        {
            "icon": "bi-house-heart",
            "name": "Residential Cleaning",
            "description": "Thorough top-to-bottom home cleaning customized to your lifestyle and preferences.",
        },
        {
            "icon": "bi-building",
            "name": "Commercial Cleaning",
            "description": "Professional office and business cleaning to create a healthy, productive workspace.",
        },
        {
            "icon": "bi-stars",
            "name": "Deep Cleaning",
            "description": "Intensive, detail-oriented cleaning that reaches every hidden corner of your space.",
        },
        {
            "icon": "bi-box-arrow-in-right",
            "name": "Move-In / Move-Out",
            "description": "Start fresh in your new home or leave your old one spotless for the next owner.",
        },
        {
            "icon": "bi-cone-striped",
            "name": "Post-Construction",
            "description": "Remove dust, debris, and construction residue after renovations or building work.",
        },
        {
            "icon": "bi-window",
            "name": "Window Cleaning",
            "description": "Crystal-clear interior and exterior window cleaning for homes and businesses.",
        },
    ]
    reviews = [
        {
            "name": "Sarah Thompson",
            "initials": "ST",
            "role": "Homeowner",
            "text": "Freshious Cleaning transformed my home! The team was professional, punctual, and incredibly thorough. My house has never been this clean!",
        },
        {
            "name": "Marcus Lee",
            "initials": "ML",
            "role": "Office Manager",
            "text": "We use Freshious for our office weekly. Consistent, reliable, and the staff are always friendly. Highly recommended for any business!",
        },
        {
            "name": "Priya Patel",
            "initials": "PP",
            "role": "Property Manager",
            "text": "Their move-out cleaning service is a game-changer. Tenants love the results and it saves me so much time. Absolutely worth every penny.",
        },
    ]
    return render(request, "home.html", {"services": services, "reviews": reviews})


def services(request):
    services_list = [
        {
            "icon": "bi-house-heart",
            "name": "Residential Cleaning",
            "description": "Comprehensive home cleaning tailored to your schedule and needs. One-time, weekly, bi-weekly, or monthly options available.",
            "features": ["Kitchen & bathrooms", "Bedrooms & living areas", "Dusting & vacuuming", "Mopping & floor care", "Trash removal"],
            "price": "From $89 / visit",
        },
        {
            "icon": "bi-building",
            "name": "Commercial Cleaning",
            "description": "Keep your workplace clean, safe, and professional with our dedicated commercial cleaning crews.",
            "features": ["Office spaces & lobbies", "Restroom sanitization", "Break room cleaning", "Trash & recycling removal", "Disinfection services"],
            "price": "From $149 / visit",
        },
        {
            "icon": "bi-stars",
            "name": "Deep Cleaning",
            "description": "A thorough, intensive clean for homes and offices that need extra attention. Includes all standard areas plus hidden spots.",
            "features": ["Behind appliances & furniture", "Inside oven & fridge", "Grout & tile scrubbing", "Baseboard & vent cleaning", "Cabinet interiors"],
            "price": "From $199 / session",
        },
        {
            "icon": "bi-box-arrow-in-right",
            "name": "Move-In / Move-Out",
            "description": "Ensure your deposit back or welcome yourself to a pristine new home. We leave nothing behind.",
            "features": ["Complete top-to-bottom clean", "Inside all cabinets & drawers", "Appliance deep clean", "Walls & doors wiped", "Garage sweep"],
            "price": "From $179 / visit",
        },
        {
            "icon": "bi-cone-striped",
            "name": "Post-Construction",
            "description": "Safely remove construction dust, debris, and residue after renovations or new builds.",
            "features": ["Dust & debris removal", "Surface wipe-down", "Window & glass cleaning", "Floor polishing", "Paint & adhesive removal"],
            "price": "Custom quote",
        },
        {
            "icon": "bi-window",
            "name": "Window Cleaning",
            "description": "Streak-free interior and exterior window cleaning using professional techniques and tools.",
            "features": ["Interior windows", "Exterior windows", "Window sills & frames", "Screen cleaning", "Glass door cleaning"],
            "price": "From $59 / visit",
        },
    ]
    addons = [
        {"icon": "bi-droplet", "name": "Carpet Shampoo", "price": "+$49"},
        {"icon": "bi-brightness-high", "name": "Oven Deep Clean", "price": "+$29"},
        {"icon": "bi-snow", "name": "Fridge Clean-Out", "price": "+$25"},
        {"icon": "bi-flower1", "name": "Odor Treatment", "price": "+$35"},
        {"icon": "bi-basket", "name": "Laundry Folding", "price": "+$20"},
        {"icon": "bi-box", "name": "Inside Cabinets", "price": "+$30"},
        {"icon": "bi-car-front", "name": "Garage Sweep", "price": "+$45"},
        {"icon": "bi-droplet-half", "name": "Pressure Washing", "price": "+$79"},
    ]
    return render(request, "services.html", {"services": services_list, "addons": addons})


def about(request):
    team = [
        {
            "name": "Maria Fresher",
            "initials": "MF",
            "role": "Co-Founder & CEO",
            "bio": "With 15 years in the industry, Maria leads the team with passion and precision.",
        },
        {
            "name": "James Fresher",
            "initials": "JF",
            "role": "Co-Founder & Operations",
            "bio": "James keeps everything running smoothly, from scheduling to quality assurance.",
        },
        {
            "name": "Lisa Park",
            "initials": "LP",
            "role": "Lead Cleaner",
            "bio": "Lisa heads our residential team and sets the gold standard for every clean.",
        },
        {
            "name": "Carlos Rivera",
            "initials": "CR",
            "role": "Commercial Lead",
            "bio": "Carlos manages our commercial division with expertise and a sharp eye for detail.",
        },
    ]
    return render(request, "about.html", {"team": team})


def contact(request):
    success = False
    if request.method == "POST":
        # In production, integrate email (e.g. Django send_mail) here
        success = True
    return render(request, "contact.html", {"success": success})
