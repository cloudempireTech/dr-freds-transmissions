// Dr. Fred's Transmissions, LLC - Interactive Engine
document.addEventListener('DOMContentLoaded', () => {
  // 1. Mobile Menu Toggle
  const mobileToggle = document.querySelector('.mobile-toggle');
  const mobileDrawer = document.querySelector('.mobile-menu-drawer');

  if (mobileToggle && mobileDrawer) {
    mobileToggle.addEventListener('click', () => {
      mobileDrawer.classList.toggle('open');
      const isOpen = mobileDrawer.classList.contains('open');
      mobileToggle.setAttribute('aria-expanded', isOpen);
    });
  }

  // 2. Dynamic Typewriter Headline
  const typewriterEl = document.querySelector('.typewriter-text');
  if (typewriterEl) {
    const phrases = [
      'ATRA Certified Rebuilds',
      'Computerized Diagnostics',
      'Torque Converter Specialists',
      'Nationwide Warranty Coverage',
      'Heavy-Duty Fleet Overhauls'
    ];
    let phraseIdx = 0;
    let charIdx = 0;
    let isDeleting = false;
    let typingSpeed = 100;

    function typeLoop() {
      const currentPhrase = phrases[phraseIdx];
      if (isDeleting) {
        typewriterEl.textContent = currentPhrase.substring(0, charIdx - 1);
        charIdx--;
        typingSpeed = 50;
      } else {
        typewriterEl.textContent = currentPhrase.substring(0, charIdx + 1);
        charIdx++;
        typingSpeed = 110;
      }

      if (!isDeleting && charIdx === currentPhrase.length) {
        typingSpeed = 2000;
        isDeleting = true;
      } else if (isDeleting && charIdx === 0) {
        isDeleting = false;
        phraseIdx = (phraseIdx + 1) % phrases.length;
        typingSpeed = 500;
      }

      setTimeout(typeLoop, typingSpeed);
    }
    typeLoop();
  }

  // 3. Animated Number Counters
  const counterEls = document.querySelectorAll('.stat-number');
  if (counterEls.length > 0) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const el = entry.target;
          const target = parseInt(el.getAttribute('data-target'), 10);
          const prefix = el.getAttribute('data-prefix') || '';
          const suffix = el.getAttribute('data-suffix') || '';
          let count = 0;
          const duration = 1800;
          const stepTime = Math.abs(Math.floor(duration / (target || 1)));

          const timer = setInterval(() => {
            count += Math.ceil(target / 45);
            if (count >= target) {
              el.textContent = `${prefix}${target.toLocaleString()}${suffix}`;
              clearInterval(timer);
            } else {
              el.textContent = `${prefix}${count.toLocaleString()}${suffix}`;
            }
          }, 35);

          observer.unobserve(el);
        }
      });
    }, { threshold: 0.2 });

    counterEls.forEach(el => observer.observe(el));
  }

  // 4. Interactive Diagnostic Symptom Intake Widget
  const calcBtn = document.getElementById('btnCalculateSymptom');
  if (calcBtn) {
    calcBtn.addEventListener('click', (e) => {
      e.preventDefault();
      const checkboxes = document.querySelectorAll('input[name="symptom"]:checked');
      const vehicleYear = document.getElementById('vehicleYear') ? document.getElementById('vehicleYear').value : '';
      const vehicleMake = document.getElementById('vehicleMake') ? document.getElementById('vehicleMake').value : '';
      const resultTitle = document.getElementById('diagResultTitle');
      const resultDesc = document.getElementById('diagResultDesc');
      const resultUrgency = document.getElementById('diagResultUrgency');

      if (checkboxes.length === 0) {
        resultTitle.textContent = "General Diagnostic Inspection";
        resultDesc.textContent = "Bring your vehicle to our Spring, TX shop for a comprehensive computer scan and hydraulic fluid test.";
        resultUrgency.innerHTML = "<strong>Status:</strong> Routine Preventive Inspection recommended.";
        return;
      }

      let symptoms = Array.from(checkboxes).map(cb => cb.value);
      
      if (symptoms.includes('slipping') || symptoms.includes('harsh')) {
        resultTitle.textContent = "Clutch / Band Slippage or Solenoid Issue";
        resultDesc.textContent = "Vehicle exhibiting slipping or harsh engagement typically indicates worn clutch packs, valve body pressure loss, or failing shift solenoids.";
        resultUrgency.innerHTML = "<strong>Urgency: Immediate Attention.</strong> Driving while slipping can cause internal clutch plate burning and torque converter failure.";
      } else if (symptoms.includes('fluid') || symptoms.includes('burning')) {
        resultTitle.textContent = "Fluid Breakdown or Hydraulic Overheating";
        resultDesc.textContent = "Burnt fluid or dark discoloration suggests severe overheating. A specialized flush, cooler line inspection, and pan inspection are required.";
        resultUrgency.innerHTML = "<strong>Urgency: High.</strong> Do not tow heavy loads until fluid inspection is complete.";
      } else if (symptoms.includes('check_engine')) {
        resultTitle.textContent = "TCM Diagnostic Trouble Codes (DTC)";
        resultDesc.textContent = "A flashing overdrive light or transmission code signals electronic sensor failure, governor pressure fault, or torque converter lockup error.";
        resultUrgency.innerHTML = "<strong>Status: Computer Scan Required.</strong> Free code reading available at Dr. Fred's shop.";
      } else {
        resultTitle.textContent = "Drivetrain Mechanical Inspection";
        resultDesc.textContent = "Noise or delayed engagement may stem from differential bearings, CV axles, transfer case chain, or fluid starvation.";
        resultUrgency.innerHTML = "<strong>Status: Inspection Recommended.</strong> Schedule a road test with our master technicians.";
      }
    });
  }
});
