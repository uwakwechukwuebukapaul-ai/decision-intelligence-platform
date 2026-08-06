"""
Intelligence Control Plane API

Management endpoints.
"""

from flask import Blueprint, jsonify

from app.intelligence.control_plane import (
    IntelligenceController,
    TaskManager,
    PolicyEngine,
    CapabilityManager,
    AuditLogger,
    HealthMonitor,
    RuntimeMetrics,
    AuditManager,
)


intelligence_control_plane_bp = Blueprint(
    "intelligence_control_plane",
    __name__,
    url_prefix="/control-plane",
)


# -----------------------------------------
# Dependency Injection
# -----------------------------------------

task_manager = TaskManager()

policy_engine = PolicyEngine()

capability_manager = CapabilityManager()

audit_logger = AuditLogger()


controller = IntelligenceController(
    task_manager=task_manager,
    policy_engine=policy_engine,
    capability_manager=capability_manager,
    audit_logger=audit_logger,
)


health = HealthMonitor()

metrics = RuntimeMetrics()

audit = AuditManager()



@intelligence_control_plane_bp.route(
    "/status",
    methods=["GET"]
)
def status():

    return jsonify(
        controller.get_status()
    )



@intelligence_control_plane_bp.route(
    "/health",
    methods=["GET"]
)
def health_check():

    return jsonify(
        health.check()
    )



@intelligence_control_plane_bp.route(
    "/metrics",
    methods=["GET"]
)
def runtime_metrics():

    return jsonify(
        metrics.get_metrics()
    )



@intelligence_control_plane_bp.route(
    "/audit",
    methods=["GET"]
)
def audit_logs():

    return jsonify(
        audit.get_events()
    )