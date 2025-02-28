document.addEventListener('DOMContentLoaded', function() {
    const quantityInput = document.querySelector('.quantity-input');
    
    if (!quantityInput || !window.location.pathname.includes('/add/')) {
        return;
    }

    const actionToggle = document.createElement('button');
    actionToggle.type = 'button';
    actionToggle.classList.add('action-toggle');
    actionToggle.dataset.value = 'add';
    actionToggle.innerText = '+';

    // Base classes
    const baseClasses = quantityInput.dataset.buttonClass;
    
    // Color classes
    const addColorClass = 'text-green-700 dark:text-green-400';
    const subtractColorClass = 'text-red-700 dark:text-red-400';
    
    // Initial state (green/add)
    actionToggle.className = `${baseClasses} ${addColorClass}`;

    const wrapper = document.createElement('div');
    wrapper.classList.add('quantity-wrapper');
    quantityInput.parentNode.insertBefore(wrapper, quantityInput);
    wrapper.appendChild(actionToggle);
    wrapper.appendChild(quantityInput);

    // Find the form that contains our quantity input
    const form = quantityInput.closest('form');

    form.addEventListener('submit', function(e) {
        // Get the raw value without any signs
        let value = quantityInput.value.replace(/[+-]/g, '');
        
        // Force sign based on current mode
        if (actionToggle.dataset.value === 'subtract') {
            value = '-' + value;
        }
        
        // Update input value before form submission
        quantityInput.value = value;
    });

    actionToggle.addEventListener('click', function() {
        const newMode = actionToggle.dataset.value === 'add' ? 'subtract' : 'add';
        
        // Update UI
        actionToggle.dataset.value = newMode;
        actionToggle.innerText = newMode === 'add' ? '+' : '-';
        actionToggle.className = `${baseClasses} ${newMode === 'add' ? addColorClass : subtractColorClass}`;
        document.querySelector('input[name="action"]').value = newMode;
    });

    // Simplify input handler to only sanitize numbers
    quantityInput.addEventListener('input', function() {
        this.value = this.value.replace(/[^\d]/g, '');
    });
});